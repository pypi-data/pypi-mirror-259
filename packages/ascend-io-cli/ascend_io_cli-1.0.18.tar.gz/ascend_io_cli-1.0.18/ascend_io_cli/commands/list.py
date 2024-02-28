from typing import Optional

import glog as log
import typer
from google.protobuf.json_format import MessageToDict

from ascend_io_cli.support import COMPONENT_PARTITIONS_METHODS, get_client, print_response

app = typer.Typer(help='Work with lists of data services, dataflows, and components', no_args_is_help=True)


@app.command()
def components(
    ctx: typer.Context,
    data_service: Optional[str] = typer.Option(None, help='Data Service id - required if using a dataflow id'),
    dataflow: Optional[str] = typer.Option(None, help='Dataflow id'),
    kind: Optional[str] = typer.Option(None, help='Component kind(source, view, sink, pub, sub)'),
    details: Optional[bool] = typer.Option(False, help='Include schema, transformation, and other details'),
):
  """List components"""
  if dataflow and not data_service:
    typer.echo('Service is required if using a flow id')
    raise typer.Exit(code=1)
  client = get_client(ctx)
  data = []
  if data_service and not dataflow:
    data = [
        MessageToDict(c) for c in client.list_data_service_components(
            data_service_id=data_service,
            deep=details,
            kind='source,view,sink,pub,sub' if not kind else kind,
        ).data
    ]
  elif dataflow:
    data = [
        MessageToDict(c) for c in client.list_dataflow_components(
            data_service_id=data_service,
            dataflow_id=dataflow,
            deep=details,
            kind='source,view,sink,pub,sub' if not kind else kind,
        ).data
    ]
  else:
    for ds in client.list_data_services().data:
      data.extend([
          MessageToDict(c) for c in client.list_data_service_components(
              data_service_id=ds.id,
              deep=details,
              kind='source,view,sink,pub,sub' if not kind else kind,
          ).data
      ])
  print_response(ctx, data)


@app.command()
def dataflows(
    ctx: typer.Context,
    data_service: str = typer.Argument(..., help='Data Service id'),
):
  """List dataflows"""
  client = get_client(ctx)
  data = []
  for df in client.list_dataflows(data_service_id=data_service).data:
    data.append(MessageToDict(df))

  print_response(ctx, data)


@app.command()
def data_services(ctx: typer.Context):
  """List data services"""
  client = get_client(ctx)
  data = []
  for ds in client.list_data_services().data:
    data.append(MessageToDict(ds))

  print_response(ctx, data)


@app.command()
def connections(
    ctx: typer.Context,
    data_service: Optional[str] = typer.Argument(None, help='Data Service id', show_default=False),
):
  """List connections available to a data service"""
  client = get_client(ctx)
  existing_connections = [c for c in client.list_connections(data_service).data]
  print_response(ctx, existing_connections)


@app.command(deprecated=True)
def partitions(
    ctx: typer.Context,
    data_service: str = typer.Argument(..., help='Data Service id', show_default=False),
    dataflow: str = typer.Argument(..., help='Dataflow id', show_default=False),
    component: str = typer.Argument(..., help='Component id', show_default=False),
    batch_size: int = typer.Option(100, help='Adjust the number of partitions to fetch per batch', hidden=True),
):
  """List the partition details for a component"""
  client = get_client(ctx)
  dataflow_components = client.list_dataflow_components(data_service, dataflow, deep=False, kind='source,view,sink').data
  found_partitions = {}
  found_components = [df for df in dataflow_components if df.id == component]
  if not found_components:
    log.warning(f"{data_service}.{dataflow}.{component} not found (must be read connector, transform, or write connector)")
    raise typer.Exit(code=1)
  for c in found_components:
    offset = 0
    method = getattr(client, COMPONENT_PARTITIONS_METHODS[c.type])
    found_partitions[c.id] = []
    # the number of partitions is unknown, fetch until there are none left
    while True:
      parts = method(data_service, dataflow, component, offset=offset, limit=batch_size).data.data.metadata
      if len(parts) == 0:
        break
      offset += len(parts)
      found_partitions[c.id].extend([MessageToDict(p) for p in parts])

  print_response(ctx, found_partitions)

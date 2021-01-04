from importlib import import_module

from typer import Typer

from protobuf2pydantic import biz

app = Typer()


# fixme
@app.command()
def pydantic(pb2_filename: str):
    module = import_module(pb2_filename)
    biz.pb2_to_pydantic(module)

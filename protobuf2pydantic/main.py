import sys
from pathlib import Path
from importlib import import_module

from typer import Typer

from protobuf2pydantic import biz

app = Typer()


@app.command()
def pydantic(pb2_path: str):
    path = Path(pb2_path).resolve()
    sys.path.append(str(path.parent))
    module = import_module(path.name.split('.')[0])
    py = biz.pb2_to_pydantic(module)
    return py

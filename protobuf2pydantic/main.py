import sys
from pathlib import Path
from importlib import import_module

from typer import Typer, echo, Argument

from protobuf2pydantic import biz

app = Typer()


@app.command()
def pydantic(
        pb2: Path = Argument(
            ...,
            exists=True,
            dir_okay=False,
            resolve_path=True,
        )
):
    sys.path.append(str(pb2.parent))
    module = import_module(pb2.stem)
    echo(biz.pb2_to_pydantic(module))

from typer.testing import CliRunner

from protobuf2pydantic.main import app

runner = CliRunner()


def test_app():
    runner.invoke(app, ["./tests/test_pb2.py"])

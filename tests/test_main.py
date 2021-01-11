from typer.testing import CliRunner

from protobuf2pydantic.main import app

runner = CliRunner()


def test_app():
    r = runner.invoke(app, ["./tests/test_pb2.py"])
    assert r.exit_code == 0

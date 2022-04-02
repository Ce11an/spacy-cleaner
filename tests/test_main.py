import typer
from typer.testing import CliRunner

from spacy_cleaner.__main__ import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--texts", "Easily clean text with spacy-cleaner!"])
    assert result.exit_code == 0
    assert "easily clean text spacy cleaner" in result.stdout


def test_version_callback():
    result = runner.invoke(app, ["-v"])
    assert result.exit_code == 0
    assert "spacy-cleaner version: " in result.stdout

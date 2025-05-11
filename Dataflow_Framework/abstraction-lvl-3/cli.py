# cli.py
import typer
from typing import Optional
from main import run

app = typer.Typer()

@app.command(name="process")
def process_command(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Optional output file path"),
    config: str = typer.Option(..., help="YAML file with pipeline configuration")
):
    run(input, output, config)

if __name__ == "__main__":
    app()

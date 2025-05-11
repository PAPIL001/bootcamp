import typer
from main import run
from typing import Optional

app = typer.Typer()

@app.command()
def process(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Optional output file path"),
    config: str = typer.Option(..., help="Pipeline config file")
):
    run(input, output, config)

if __name__ == "__main__":
    app()

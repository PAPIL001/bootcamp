import typer
from typing import Optional

app = typer.Typer()

@app.command()
def process(
    input: str = typer.Option(..., "--input", "-i", help="Input file path"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path"),
    mode: Optional[str] = typer.Option(None, "--mode", "-m", help="Processing mode (uppercase or snakecase)")
):
    from main import run
    run(input, output, mode)

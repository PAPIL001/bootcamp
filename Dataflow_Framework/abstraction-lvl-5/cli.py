import typer
from main import run

app = typer.Typer()

@app.command()
def process(input: str, config: str):
    """
    Process the input file using the given pipeline config.
    """
    run(input, config)

if __name__ == "__main__":
    import sys
    app(prog_name="cli.py")


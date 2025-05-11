import click
from pathlib import Path
from engine.processors import process_file

@click.command()
@click.argument("file_path")
def cli(file_path):
    process_file(Path(file_path))

if __name__ == "__main__":
    cli()

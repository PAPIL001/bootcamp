import typer
import yaml
from router import Router

app = typer.Typer()

def read_lines(path: str):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def read_config(path: str):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

@app.command()
def run_pipeline(input_file: str, config_file: str):
    """
    Run the dataflow pipeline using input lines and YAML config.
    """
    try:
        lines = read_lines(input_file)
        config = read_config(config_file)
        router = Router(config)
        router.run('start', lines)
    except Exception as e:
        typer.echo(f"❌ Error: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()

import os
from typing import Optional, Iterator
from dotenv import load_dotenv
import typer

load_dotenv()  # Load environment variables from .env file

def read_lines(file_path: str) -> Iterator[str]:
    """
    Reads lines from a file, yielding each line with leading/trailing whitespace removed.

    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")
        

def write_output(lines: Iterator[str], output_path: Optional[str] = None) -> None:
    """
    Writes the transformed lines to a file or prints them to the console.

    """
    if output_path:
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line + '\n')
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    else:
        for line in lines:
            print(line)

def get_mode_from_env() -> str:
    """
    Gets the processing mode from the environment variable 'MODE'.
    Defaults to 'uppercase' if not set.

    """
    return os.getenv("MODE", "uppercase")


def run(input_path: str, output_path: Optional[str] = None, mode: Optional[str] = None) -> None:
    
    mode = mode or get_mode_from_env()
    try:
        #  Verify that get_pipeline and apply_processors are actually defined and behave as expected.
        processors = get_pipeline(mode)  #  moved inside the try block
        lines = (apply_processors(line, processors) for line in read_lines(input_path)) #  moved inside the try block
        write_output(lines, output_path)
        typer.echo("Pipeline execution completed.")

    except FileNotFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except IOError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(1)



if __name__ == "__main__":
    import cli
    cli.app()  # Assumes cli.app() is the Typer application.


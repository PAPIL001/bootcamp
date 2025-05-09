import typer
from typing import Optional, Iterator
from dotenv import load_dotenv
import os

app = typer.Typer()
load_dotenv()  # Load environment variables from .env file

def read_lines(file_path: str) -> Iterator[str]:
    """
    Reads lines from a file, yielding each line with leading/trailing whitespace removed.

    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:  # Explicit encoding
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")

def transform_line(text: str, mode: str) -> str:
    """
    Transforms a string based on the specified mode.

    """
    mode = mode.lower() # added to handle if user provides Uppercase
    if mode == 'uppercase':
        return text.upper()
    elif mode == 'snakecase':
        return text.replace(' ', '_').lower()
    else:
        raise ValueError(f"Error: Unsupported mode '{mode}'.  Valid modes are 'uppercase' or 'snakecase'.")

def write_output(lines: Iterator[str], output_path: Optional[str] = None) -> None:
    """
    Writes the transformed lines to a file or prints them to the console.

    """
    if output_path:
        try:
            with open(output_path, 'w', encoding='utf-8') as f:  # Explicit encoding
                for line in lines:
                    f.write(line + '\n')
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    else:
        for line in lines:
            print(line)

def get_mode_from_env() -> str:
    mode = os.getenv("MODE", "uppercase")
    return mode

@app.command()
def process_text(
    input_file: str = typer.Option(..., help="Path to the input file."),
    output_file: Optional[str] = typer.Option(None, help="Optional path to the output file."),
    mode: Optional[str] = typer.Option(None, help="Processing mode ('uppercase' or 'snakecase')."),
):
    
    mode = mode or get_mode_from_env()  # gets the mode.
    try:
        lines = read_lines(input_file)
        processed_lines = (transform_line(line, mode) for line in lines)
        write_output(processed_lines, output_file)
        typer.echo(f"Text processing complete. Mode: {mode}") # Added message.
    except (FileNotFoundError, IOError, ValueError) as e:
        typer.echo(f"Error: {e}", err=True)  # Use typer.echo for errors
        raise typer.Exit(1)  # Use typer.Exit for consistent error handling

if __name__ == "__main__":
    app()

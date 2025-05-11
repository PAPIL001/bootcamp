# Abstraction Level 1

## Overview

In **Level 1**, the script evolves from a one-off solution to a configurable tool. It introduces basic **command-line arguments** and a **parameterized interface**, making the tool more flexible.

## How it works

The `process.py` script:

* Accepts command-line arguments via **Typer**:

  * `--input`: Required parameter specifying the input file path
  * `--output`: Optional parameter specifying the output file path
  * `--mode`: Optional parameter specifying the processing mode (defaults to `uppercase` via `.env`)
* Loads default values (like `mode`) from a `.env` file using `python-dotenv`
* Supports two modes of text transformation:

  * **uppercase**: Converts each line to uppercase
  * **snakecase**: Replaces spaces with underscores and converts to lowercase
* Processes each line according to the selected mode and writes the result to the output (or prints to `stdout` if no output file is specified)

## Usage

Run the script with the required `--input` argument, and optional `--output` and `--mode` arguments:

```bash

# To use snakecase mode
python process.py --input input.txt --mode snakecase

# To specify an output file
python process.py --input input.txt --output output.txt
```

## Sample Input and Output


### Sample Input 1 (`input.txt`)

```
hello world
```

### Sample Output 1 (`--mode snakecase`)

```
hello_world
```

## Abstraction Level 1

This level introduces basic **parameterization** and **configuration**:

* The script is now configurable via **command-line arguments** (`--input`, `--output`, `--mode`).
* It loads configuration defaults (like `mode`) from a `.env` file using the `python-dotenv` package.
* Basic string transformations (uppercase and snakecase) are applied based on the chosen mode.
* Functions like `read_lines()`, `transform_line()`, and `write_output()` help in breaking up the logic into smaller, reusable parts — preparing the code for further abstraction in the next level.

---


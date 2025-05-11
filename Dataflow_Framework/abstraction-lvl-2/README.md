# Abstraction Level 2

A command-line application that reads lines from an input file, applies a configurable pipeline of transformations, and writes or prints the results.

---

## Project Structure

```

dataflow-framework/
│
├── abstraction-level-2/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   ├── core.py
│   ├── pipeline.py
│   ├── types.py
│   ├── input.txt
│   ├── .env
│   ├── README.md
│   └── requirements.txt
└── ...

````

---

## Running the CLI

> **Make sure you're in the root directory of the project:**
>  
> ```bash
> cd ~/bootcamp/days/dataflow-framework
> ```

Then use:

```bash
python -m abstraction-level-2.main --input abstraction-level-2/input.txt
````

### Available CLI Options

| Option             | Description                                    | Example                                 |
| ------------------ | ---------------------------------------------- | --------------------------------------- |
| `--input` or `-i`  | Path to the input file                         | `--input abstraction-level-2/input.txt` |
| `--output` or `-o` | (Optional) Path to the output file             | `--output output.txt`                   |
| `--mode` or `-m`   | (Optional) Processing mode (e.g., `uppercase`) | `--mode uppercase`                      |

You can combine them as needed:

```bash
python -m abstraction-level-2.main --input abstraction-level-2/input.txt --output abstraction-level-2/output.txt --mode uppercase
```

---

## Sample Input (input.txt)

```
hello world
```

---

## Sample Output (stdout or output.txt if specified)

```
HELLO WORLD
```

---

## Installing Requirements

Create a virtual environment and install dependencies:

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

**requirements.txt**

```
typer==0.12.3
rich==13.7.1
python-dotenv==1.0.1
```

---

## Notes

* The CLI should **always be run from the root** of the project (`dataflow-framework/`).
* Input and output file paths should be relative to that root.


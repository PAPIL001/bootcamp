# Basic scripts

## Overview

This is the starting point of the **Streaming Line Processing** journey — a minimal, no-abstraction script that performs a basic text transformation. It reads from standard input, processes each line, and prints the output.

## How it works

The `process.py` script:

* Reads text line by line from `stdin`
* Removes leading and trailing whitespace
* Converts each line to uppercase
* Outputs the result to `stdout`

## Usage

Pipe any text into the script like this:

```bash
echo "  hEy there " | python process.py
# Output: HEY THERE
```

Or process text from a file:

```bash
cat input.txt | python process.py
```

#### Sample Input (`sample.txt`)

```
 hello
```

#### Sample Output

```
HELLO
```

---


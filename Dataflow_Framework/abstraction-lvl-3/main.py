# main.py
from pipeline import load_pipeline
from core import process_lines

def run(input_path: str, output_path: str, config_path: str):
    processors = load_pipeline(config_path)
    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    processed = process_lines(lines, processors)

    if output_path:
        with open(output_path, 'w') as outfile:
            outfile.writelines(processed)
    else:
        for line in processed:
            print(line, end="")

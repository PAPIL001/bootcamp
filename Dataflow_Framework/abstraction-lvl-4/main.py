from pipeline import load_pipeline
from core import run_pipeline

def run(input_path: str, output_path: str, config_path: str):
    processors = load_pipeline(config_path)
    with open(input_path, 'r') as f:
        lines = f.readlines()

    result = run_pipeline(iter(lines), processors)

    if output_path:
        with open(output_path, 'w') as f:
            for line in result:
                f.write(line + "\n")
    else:
        for line in result:
            print(line)

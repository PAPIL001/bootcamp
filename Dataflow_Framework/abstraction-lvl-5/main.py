from pipeline import load_pipeline

def run(input_path: str, config_path: str):
    dag = load_pipeline(config_path)

    with open(input_path, 'r') as f:
        for line in f:
            dag.process(line.strip())

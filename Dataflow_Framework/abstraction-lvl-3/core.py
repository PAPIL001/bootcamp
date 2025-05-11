# core.py
from processor_types import ProcessorFn

def process_lines(lines: list[str], processors: list[ProcessorFn]) -> list[str]:
    for processor in processors:
        lines = [processor(line) for line in lines]
    return lines

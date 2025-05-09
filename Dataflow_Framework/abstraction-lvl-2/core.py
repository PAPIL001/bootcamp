from processor_types import ProcessorFn

def to_uppercase(line: str) -> str:
    return line.strip().upper()

def to_snakecase(line: str) -> str:
    return line.strip().replace(" ", "_").lower()

def apply_processors(line: str, processors: list[ProcessorFn]) -> str:
    for processor in processors:
        line = processor(line)
    return line

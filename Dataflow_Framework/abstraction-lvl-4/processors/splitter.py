from typing import Iterator
from processor_types import StreamProcessor

class Splitter:
    def __init__(self, delimiter: str):
        self.delimiter = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            parts = line.strip().split(self.delimiter)
            for part in parts:
                yield part

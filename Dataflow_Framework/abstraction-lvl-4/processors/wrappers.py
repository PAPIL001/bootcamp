from typing import Iterator, Callable
from processor_types import StreamProcessor

def wrap_str_processor(fn: Callable[[str], str]) -> StreamProcessor:
    def processor(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield fn(line)
    return processor

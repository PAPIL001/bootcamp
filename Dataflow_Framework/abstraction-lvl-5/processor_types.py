from typing import Iterator, Tuple

TaggedLine = Tuple[str, str]  # (tag, line)
Processor = Callable[[str], Iterator[TaggedLine]]

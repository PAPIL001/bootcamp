from typing import Iterator, Callable

StreamProcessor = Callable[[Iterator[str]], Iterator[str]]

from core import to_uppercase, to_snakecase
from processor_types import ProcessorFn
from dotenv import load_dotenv
import os

load_dotenv()

def get_pipeline(mode: str) -> list[ProcessorFn]:
    if mode == "snakecase":
        return [to_snakecase]
    return [to_uppercase] #default
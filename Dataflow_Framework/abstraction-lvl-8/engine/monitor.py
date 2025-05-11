import os
import shutil
import time
from pathlib import Path
import threading
from engine.processors import process_file
from engine.tracing import trace

WATCH_DIR = Path("watch_dir")
UNPROCESSED_DIR = WATCH_DIR / "unprocessed"
UNDERPROCESS_DIR = WATCH_DIR / "underprocess"
PROCESSED_DIR = WATCH_DIR / "processed"

# Ensure required directories exist
for directory in [UNPROCESSED_DIR, UNDERPROCESS_DIR, PROCESSED_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

def start_monitoring(file_path):
    """ Start monitoring the folder for new files """
    while True:
        for file_path in UNPROCESSED_DIR.iterdir():
            if file_path.is_file():
                trace(f"New file detected: {file_path.name}")
                process_file(file_path)
        time.sleep(5)  # Check for new files every 5 seconds

def restart_on_crash():
    """ Handle system crash and retry logic """
    for file_path in UNDERPROCESS_DIR.iterdir():
        if file_path.is_file():
            shutil.move(file_path, UNPROCESSED_DIR / file_path.name)
    trace("System restarted, files in underprocess/ moved to unprocessed/")

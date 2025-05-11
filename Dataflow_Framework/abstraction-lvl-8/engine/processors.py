import shutil
import threading
import time
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory paths
UNPROCESSED_DIR = Path("watch_dir/unprocessed")
UNDERPROCESS_DIR = Path("watch_dir/underprocess")
PROCESSED_DIR = Path("watch_dir/processed")
FAILED_DIR = Path("watch_dir/failed_files")

# Retry config
MAX_RETRIES = 3

# FastAPI app
app = FastAPI()

# Model for dashboard
class FileStatus(BaseModel):
    filename: str
    status: str

# In-memory file status tracker
file_status = []

@app.post("/update-status/")
async def update_status(status: FileStatus):
    file_status.append(status.dict())
    return {"message": "Status updated successfully"}

@app.get("/file-status/")
async def get_status():
    return {"files": file_status}


# ----------------------------
# File Processing Logic
# ----------------------------

def process_line(line: str):
    return line.strip().upper() or None

def update_file_status(file_path, status):
    try:
        requests.post("http://127.0.0.1:8000/update-status/", json={
            "filename": file_path.name,
            "status": status
        })
    except Exception as e:
        logger.warning(f"Could not update status: {e}")

def process_file(file_path: Path):
    """Processes the file and moves it to processed or failed folder."""
    try:
        filename = file_path.name
        temp_path = UNDERPROCESS_DIR / filename

        logger.info(f"🚀 Processing file: {file_path}")
        shutil.move(file_path, temp_path)
        update_file_status(file_path, "underprocess")

        with open(temp_path, "r") as f:
            for line in f:
                result = process_line(line)
                if result:
                    print(result)

        shutil.move(temp_path, PROCESSED_DIR / filename)
        logger.info(f"✅ Processed: {filename}")
        update_file_status(file_path, "processed")

    except Exception as e:
        logger.error(f"❌ Error processing {file_path}: {e}")
        update_file_status(file_path, "failed")
        if 'temp_path' in locals() and temp_path.exists():
            shutil.move(temp_path, FAILED_DIR / temp_path.name)

def process_file_with_retry(file_path: Path, retries=0):
    try:
        process_file(file_path)
    except Exception as e:
        if retries < MAX_RETRIES:
            logger.warning(f"Retrying {file_path} ({retries+1}/{MAX_RETRIES})")
            process_file_with_retry(file_path, retries + 1)
        else:
            logger.error(f"❌ Failed permanently: {file_path}")
            shutil.move(file_path, FAILED_DIR / file_path.name)

def process_file_thread(file_path: Path):
    threading.Thread(target=process_file_with_retry, args=(file_path,), daemon=True).start()


# ----------------------------
# Recovery + Watch Loop
# ----------------------------

def recover_unfinished_files():
    for file in UNDERPROCESS_DIR.glob("*.txt"):
        logger.info(f"🔁 Recovering: {file}")
        process_file_thread(file)

def run_forever():
    recover_unfinished_files()
    while True:
        for file in UNPROCESSED_DIR.glob("*.txt"):
            process_file_thread(file)
        time.sleep(1)


# ----------------------------
# Entry point
# ----------------------------

if __name__ == "__main__":
    # Start FastAPI dashboard in background
    api_thread = threading.Thread(
        target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info"),
        daemon=True
    )
    api_thread.start()

    # Start the processing loop
    run_forever()

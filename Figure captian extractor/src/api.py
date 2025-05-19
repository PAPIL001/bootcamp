# src/api.py
from typing import List, Dict, Any, Optional

from fastapi import FastAPI, HTTPException, File, UploadFile, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

from src.data_storage import DataStorage  # Import your DataStorage class

# --- Data Models ---
class ExtractionRequest(BaseModel):
    paper_ids: List[str]

class PaperData(BaseModel):
    pmc_id: str
    pmid: Optional[str] = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    figure_captions: List[Dict[str, Any]] = None # Each caption might have text and entities
    figure_urls: Optional[List[str]] = None # You might need to adjust this based on your storage

# --- Security ---
security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    # In a real application, you would validate these against stored credentials
    if credentials.username == "admin" and credentials.password == "your_admin_password":
        return credentials.username
    raise HTTPException(status_code=401, detail="Invalid credentials")

# --- FastAPI Application ---
app = FastAPI()
data_storage = DataStorage() # Instantiate DataStorage here

@app.post("/submit", dependencies=[Depends(get_current_user)])
async def submit_ids(request: ExtractionRequest):
    """
    Submits a list of paper IDs for extraction.
    """
    # TODO: Implement the logic to trigger the ingestion pipeline
    # For now, let's just return a success message
    # The ingestion pipeline will use data_storage to save the results
    return {"message": f"Extraction initiated for paper IDs: {request.paper_ids}"}

@app.get("/data/{paper_id}", response_model=Optional[PaperData], dependencies=[Depends(get_current_user)])
async def get_paper_data(paper_id: str):
    """
    Retrieves the extracted data for a given paper ID (currently only paper metadata).
    """
    paper_info = data_storage.get_paper_data(paper_id)
    if paper_info:
        return PaperData(**paper_info)
    raise HTTPException(status_code=404, detail=f"Paper with ID {paper_id} not found")

@app.post("/upload", dependencies=[Depends(get_current_user)])
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a file containing a list of paper IDs for extraction.
    """
    try:
        contents = await file.read()
        ids = contents.decode().strip().splitlines()
        # TODO: Implement logic to trigger ingestion for these IDs
        return {"message": f"Extraction initiated for IDs from uploaded file: {ids}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing uploaded file: {e}")

@app.get("/health")
async def health_check():
    """
    Basic health check endpoint.
    """
    return {"status": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
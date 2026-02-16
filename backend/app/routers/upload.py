from fastapi import APIRouter, UploadFile, File
import shutil
from app.config import SEARCH_CONSOLE_PATH, GA4_PATH

router = APIRouter(prefix="/upload")

@router.post("/search-console")
def upload_search_console(file: UploadFile = File(...)):
    with open(SEARCH_CONSOLE_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Search Console data uploaded successfully"}

@router.post("/ga4")
def upload_ga4(file: UploadFile = File(...)):
    with open(GA4_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "GA4 data uploaded successfully"}

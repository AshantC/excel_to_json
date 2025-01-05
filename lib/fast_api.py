from fastapi import FastAPI, HTTPException, Depends
from .file_converter import FileConverter, get_conversion

app = FastAPI(title="File Conversion", docs_url="/")

@app.get("/")
async def read_root():
    return {"message":"Welcome to the file conversion"}

@app.get("/convert-file")
async def trigger():
    return {"message": "Initiating Trigger"}
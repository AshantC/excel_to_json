from fastapi import FastAPI, HTTPException, Depends
from .file_converter import FileConverter, get_converter
import os

app = FastAPI(title="File Conversion", docs_url="/")

@app.get("/convert-file")
async def trigger(initiator:str, output_dir: str, app:FileConverter=Depends(get_converter)):
    input_dir = os.getenv("SOURCE_DIR")
    output_dir = os.path.join("Files/",output_dir)
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        if not os.path.exists(input_dir):
            raise HTTPException(status_code=400, detail="Input directory does not exit.")
        else:
            app.conversion(input_dir, output_dir)
    except Exception as e:
        raise HTTPException(status_code=500, detail={e})
    
    return {"message": "File conversion triggered", "initiator":f"{initiator}"}

@app.get("/all-files")
async def all_files(app: FileConverter = Depends(get_converter)):
    input_dir = os.getenv("SOURCE_DIR")
    output_dir = os.getenv("OUTPUT_DIR")
    try:
        os.makedirs(output_dir, exist_ok=True)
        if not os.path.exists(input_dir):
            raise HTTPException(status_code=400, detail="Input directory does not exist.")
        else:
            app.file_name(input_dir)
    except Exception as e:
        print(f"Something went wrong: {e}")
    else:
        print("Focus")
    return {"message":"Generating Files"}
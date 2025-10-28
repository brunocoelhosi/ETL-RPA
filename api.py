from fastapi import FastAPI, File
from fastapi import UploadFile
from rpa import process_curriculum
from typing import List
app = FastAPI()
from openpyxl import Workbook
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/process")
async def process(files: List[UploadFile] = File(...)):


    wb = Workbook()
    ws = wb.active
    ws.title = "PDF Imports"

    ws.append(["Name", "File", "Age", "Hard Skills"])

    results = []

    file_infos = []
    
    for file in files:
        info = process_curriculum(file)
        ws.append([info["name"], info["file"], info["age"], ", ".join(info["skills"])])
        results.append(info)

    wb.save("curriculos_processados.xlsx")

    return {"uploaded_files": file_infos}

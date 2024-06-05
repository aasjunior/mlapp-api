from fastapi import APIRouter, HTTPException, status, UploadFile, File
from model.schemas import DataScheme
from model.DataModel import DataModel

router = APIRouter()

@router.post("/knn")
async def knn(data: DataScheme, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        data_model = DataModel(contents, data.attributeHeaders, data.classHeader)
        result = apply_knn(data_model)
        return {"result": result}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))

@router.get("/genetic-algorithm")
async def genetic_algorithm():
    return "Genetic Algorithm"
from fastapi import APIRouter, HTTPException, status, UploadFile, File
from model.DataScheme import DataScheme
from service.knn import apply_knn
from model.DataModel import DataModel
import pandas as pd

router = APIRouter()

@router.post("/knn")
async def knn(data: DataScheme, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(contents)
        X = df[list(data.attributeHeaders)]
        y = df[data.classHeader]

        accuracy = apply_knn(X, y)

        info = {
            "quantidade de exemplos": len(df),
            "quantidade de classes": df[data.classHeader].nunique(),
            "quantidade de atributos": len(data.attributeHeaders),
            "taxa de acerto": "%.2f%%" % accuracy,
        }

        return {"result": info}

    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))

@router.get("/genetic-algorithm")
async def genetic_algorithm():
    return "Genetic Algorithm"
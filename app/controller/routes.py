from fastapi import APIRouter, HTTPException, status, UploadFile, File
from model.DataScheme import DataScheme
from service.knn import apply_knn
import pandas as pd

router = APIRouter()

@router.post('/knn')
async def knn(data: DataScheme, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(contents)
        X = df[list(data.attributeHeaders)]
        y = df[data.classHeader]

        accuracy = apply_knn(X, y)

        info = {
            'quantidade de exemplos': len(df),
            'quantidade de classes': df[data.classHeader].nunique(),
            'quantidade de atributos': len(data.attributeHeaders),
            'taxa de acerto': '%.2f%%' % accuracy,
        }

        return {'result': info}

    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))

@router.get('/test-knn')
async def test_knn():
    attribute_headers = ['sepal_length','sepal_width','petal_length','petal_width']
    class_header = 'class'
    try:

        df = pd.read_csv('db/iris.csv')
        X = df[list(attribute_headers)]
        y = df[class_header]

        accuracy = apply_knn(X, y)

        info = {
            'quantidade de exemplos': len(df),
            'quantidade de classes': df[class_header].nunique(),
            'quantidade de atributos': len(attribute_headers),
            'taxa de acerto': accuracy,
        }

        return {'result': info}

    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@router.get("/genetic-algorithm")
async def genetic_algorithm():
    return "Genetic Algorithm"
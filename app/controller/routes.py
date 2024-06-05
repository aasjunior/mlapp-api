from fastapi import APIRouter, HTTPException, status, UploadFile, File
from model.DataScheme import DataScheme
from service.knn import apply_knn
from service.decision_tree import apply_decision_tree
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
            'number_of_examples': len(df),
            'number_of_classes': df[data.classHeader].nunique(),
            'number_of_attributes': len(data.attributeHeaders),
            'accuracy': '%.2f%%' % accuracy,
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
            'number_of_examples': len(df),
            'number_of_classes': df[class_header].nunique(),
            'number_of_attributes': len(attribute_headers),
            'accuracy': accuracy,
        }

        return {'result': info}

    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@router.post('/decision-tree')
async def decision_tree(data: DataScheme, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(contents)
        X = df[list(data.attributeHeaders)]
        y = df[data.classHeader]

        result = apply_decision_tree(X, y)

        info = {
            'number_of_examples': len(df),
            'number_of_classes': df[data.classHeader].nunique(),
            'number_of_attributes': len(data.attributeHeaders),
            'model_info': result
        }

        return {'result': info}

    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@router.get('/test-decision-tree')
async def test_decision_tree():
    attribute_headers = ['sepal_length','sepal_width','petal_length','petal_width']
    class_header = 'class'

    try:
        df = pd.read_csv('db/iris.csv')
        X = df[list(attribute_headers)]
        y = df[class_header]

        result = apply_decision_tree(X, y)

        info = {
            'number_of_examples': len(df),
            'number_of_classes': df[class_header].nunique(),
            'number_of_attributes': len(attribute_headers),
            'model_info': result
        }

        return {'result': info}
    
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@router.get("/genetic-algorithm")
async def genetic_algorithm():
    return "Genetic Algorithm"
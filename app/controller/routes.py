from fastapi import APIRouter, HTTPException, status, UploadFile, File
from model.DataScheme import DataScheme
from service.knn import apply_knn
from service.decision_tree import apply_decision_tree
from service.genetic_algorithm import apply_genetic_algorithm
from service.utils import generate_log
import pandas as pd
import traceback

router = APIRouter()

data_src = "assets/db/iris.csv"

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
        generate_log(e, traceback.format_exc())
        return HTTPException(status_code=400, detail=str(e))


@router.get('/test-knn')
async def test_knn():
    attribute_headers = ['sepal_length','sepal_width','petal_length','petal_width']
    class_header = 'class'
    
    try:
        df = pd.read_csv(data_src)
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
        generate_log(e, traceback.format_exc())
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
        generate_log(e, traceback.format_exc())
        return HTTPException(status_code=400, detail=str(e))


@router.get('/test-decision-tree')
async def test_decision_tree():
    attribute_headers = ['sepal_length','sepal_width','petal_length','petal_width']
    class_header = 'class'

    try:
        df = pd.read_csv(data_src)
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
        generate_log(e, traceback.format_exc())
        return HTTPException(status_code=400, detail=str(e))


@router.get("/genetic-algorithm")
async def genetic_algorithm():
    try:
        info = apply_genetic_algorithm()
        return {'result': info}
    
    except Exception as e:
        generate_log(e, traceback.format_exc())
        return HTTPException(status_code=400, detail=str(e))

    
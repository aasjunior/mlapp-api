from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pandas import DataFrame, Series
from base64 import b64encode
import matplotlib.pyplot as plt
from io import BytesIO
import joblib

def apply_decision_tree(X: DataFrame, y: Series, test_size=0.3, train_size=0.7):
    try:
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, train_size=train_size)

        dt_classifier = DecisionTreeClassifier()
        dt_classifier.fit(X_train, Y_train)

        predictions = dt_classifier.predict(X_test)
        accuracy = accuracy_score(Y_test, predictions) * 100

        plot_decision_tree(dt_classifier)
        model_image_base64 = get_image_base64('db/plot/tree.png')
        
        model_info = {
            'accuracy': '%.2f%%' % accuracy,
            'model': model_serialize(dt_classifier),
            'model_image': model_image_base64
        }

        return model_info
    
    except Exception as e:
        raise Exception(f'\nOcorreu um erro na execução da arvore de decisão:\n{e}\n')

import io

def model_serialize(dt_classifier: DecisionTreeClassifier):
    buffer = BytesIO()
    joblib.dump(dt_classifier, buffer)
    buffer.seek(0)
    model_bytes = buffer.read()

    model_base64 = b64encode(model_bytes).decode('utf-8')

    return model_base64


def plot_decision_tree(dt_classifier: DecisionTreeClassifier):
    fig, ax = plt.subplots(figsize=(20, 20))  # Ajuste o tamanho conforme necessário
    plot_tree(dt_classifier, filled=True, ax=ax)
    plt.savefig('db/plot/tree.png', format='png')


def get_image_base64(image_path: str):
    with open(image_path, 'rb') as img_file:
        return b64encode(img_file.read()).decode('utf-8')
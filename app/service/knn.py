from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pandas import DataFrame
import pandas as pd


def apply_knn(X: DataFrame, y: DataFrame, test_size=0.3, train_size=0.7, n_neighbors=3):
    try:
        X, y = normalize_data(X, y)

        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, train_size=train_size)

        knn = KNeighborsClassifier(n_neighbors)
        knn.fit(X_train, Y_train)

        predictions = knn.predict(X_test)
        accuracy = accuracy_score(Y_test, predictions) * 100

        return  "%.2f%%" % accuracy
    
    except Exception as e:
        raise Exception("\nOcorreu um erro na execução do Knn:\n{e}\n")

def normalize_data(X: DataFrame, y: DataFrame):
    encoder = LabelEncoder()
    scaler = MinMaxScaler()
    
    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = encoder.fit_transform(X[col])
    
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    if y.dtype == 'object':
        y = encoder.fit_transform(y)
        y = pd.Series(y.flatten())
    
    return X, y


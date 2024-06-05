from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pandas import DataFrame, Series

def apply_decision_tree(X: DataFrame, y: Series, test_size=0.3, train_size=0.7):
    try:
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, train_size=train_size)

        dt_classifier = DecisionTreeClassifier()
        dt_classifier.fit(X_train, Y_train)

        predictions = dt_classifier.predict(X_test)
        accuracy = accuracy_score(Y_test, predictions) * 100

        return '%.2f%%' % accuracy
    
    except Exception as e:
        raise Exception('\nOcorreu um erro na execução da arvore de decisão:\n{e}\n')

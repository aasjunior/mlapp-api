from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from .utils import generate_unique_filename, get_image_base64, ensure_directory_exists
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
    fig, ax = plt.subplots(figsize=(20, 20))
    plot_tree(dt_classifier, filled=True, ax=ax)

    fig_name = generate_unique_filename()
    plt.savefig(f'db/plot/{fig_name}', format='png')


def describe_decision_tree(tree_model, feature_names):
    # Obtém os nós da árvore
    tree_nodes = tree_model.tree_

    def describe_node(node_index):
        if tree_nodes.children_left[node_index] == tree_nodes.children_right[node_index]:
            # Nó folha
            class_counts = tree_nodes.value[node_index][0]
            class_labels = [f"Classe {i}" for i in range(len(class_counts))]
            node_description = f"Nó folha: Contagem de amostras por classe: {dict(zip(class_labels, class_counts))}"
        else:
            # Nó interno
            feature_index = tree_nodes.feature[node_index]
            threshold = tree_nodes.threshold[node_index]
            left_child = tree_nodes.children_left[node_index]
            right_child = tree_nodes.children_right[node_index]
            node_description = f"Nó interno: Característica {feature_names[feature_index]}, Threshold: {threshold:.2f}, Filhos: Esquerda ({left_child}), Direita ({right_child})"

        return node_description

    root_description = describe_node(0)
    return root_description
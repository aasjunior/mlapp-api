from model.DataModel import DataModel
from model.KNNModel import KNNModel

def apply_knn(data_model: DataModel):
    knn_model = KNNModel(data_model, neighboor=3)

    

    accuracy = knn_model.train_and_evaluate()
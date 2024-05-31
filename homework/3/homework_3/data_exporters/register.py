import mlflow
from mlflow.tracking import MlflowClient
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(data, *args, **kwargs):
    dv = data[0]
    lr = data[1]
    client = MlflowClient()
    experiment = client.get_experiment_by_name("homework-3")

    # Log the model (linear regression)
    mlflow.sklearn.log_model(lr, artifact_path="lr_model")
    # Save and log the artifact (dict vectorizer)
    with open('lr-vectorizer.bin', 'wb') as f_out:
        pickle.dump(dv, f_out)
    mlflow.log_artifact("lr-vectorizer.bin")

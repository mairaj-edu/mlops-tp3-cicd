"""
Script d'entraînement + enregistrement dans MLflow Model Registry.
À exécuter après avoir démarré le serveur MLflow :
    mlflow server --host 127.0.0.1 --port 5000
"""

import mlflow
import mlflow.sklearn
from src.train import train
from src.data import load_params

params = load_params()
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment(params["training"]["experiment_name"])

with mlflow.start_run(run_name="sentiment-baseline") as run:
    model, metrics = train()

    mlflow.log_params(params["model"])
    mlflow.log_metrics(metrics)

    # Log du modèle scikit-learn
    mlflow.sklearn.log_model(model, artifact_path="model")

    # Enregistrement dans le Model Registry
    model_uri = f"runs:/{run.info.run_id}/model"
    result = mlflow.register_model(
        model_uri,
        params["training"]["model_name"]
    )

    print(f"   Modèle enregistré → version {result.version}")
    print(f"   Accuracy : {metrics['accuracy']:.3f} | F1 : {metrics['f1']:.3f}")
    print(f"   Run ID   : {run.info.run_id}")

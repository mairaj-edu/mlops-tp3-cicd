"""
Script de promotion d'un modèle dans le Model Registry.
Usage :
    python promote.py
"""

from mlflow.tracking import MlflowClient
from src.data import load_params

params = load_params()
client = MlflowClient(tracking_uri="http://127.0.0.1:5000")
model_name = params["training"]["model_name"]

versions = client.search_model_versions(f"name='{model_name}'")
if not versions:
    raise RuntimeError(
        f"Aucun modèle trouvé avec le nom '{model_name}'. "
        "Exécutez d'abord train_and_register.py"
    )

latest = max(versions, key=lambda v: int(v.version))
print(f"Version actuelle : {latest.version} | Stage : {latest.current_stage}")

# Promotion vers Staging
client.transition_model_version_stage(
    name=model_name,
    version=latest.version,
    stage="Staging"
)
print(f"✅ Version {latest.version} promue en Staging")
print("   Vérifiez dans l'UI MLflow : http://127.0.0.1:5000/#/models")

# Pour simuler une approbation humaine avant Production, décommentez :
# input("Appuyez sur Entrée après validation humaine pour passer en Production...")
# client.transition_model_version_stage(
#     name=model_name,
#     version=latest.version,
#     stage="Production"
# )
# print(f"✅ Version {latest.version} promue en Production")

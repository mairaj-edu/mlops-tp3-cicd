# TP3 – Module 3 : CI/CD, Tests et Gouvernance des Modèles

## Objectifs

- Mettre en place un pipeline CI/CD avec GitHub Actions
- Implémenter différents types de tests (unitaires, données, modèle, LLM)
- Utiliser le MLflow Model Registry avec stratégie de promotion
- Intégrer des guardrails de base
- Comprendre la gouvernance des modèles en environnement industriel

> **Cas d’usage :** classification de sentiment simple (scikit-learn).

---

## Structure du projet

```
mlops-tp3-cicd/
├── .github/workflows/mlops-pipeline.yml
├── data/reviews.csv
├── src/
│   ├── data.py
│   ├── model.py
│   └── train.py
├── tests/
│   ├── test_unit.py
│   ├── test_data.py
│   ├── test_model.py
│   └── test_llm.py
├── params.yaml
├── requirements.txt
├── train_and_register.py
├── promote.py
└── README.md
```

---

## Installation rapide

```bash
python -m venv .venv
source .venv/bin/activate         
pip install -r requirements.txt
```

---

## Checkpoints

### Checkpoint 1 – Tests locaux
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```
→ Tous les tests doivent passer.

### Checkpoint 2 – MLflow
Dans un terminal :
```bash
mlflow server --host 127.0.0.1 --port 5000
```

Dans un autre :
```bash
python train_and_register.py
python promote.py
```
→ Le modèle `sentiment-model` doit apparaître en stage **Staging** sur http://127.0.0.1:5000

### Checkpoint 3 – GitHub Actions
1. Créez un repository GitHub
2. Poussez le code
3. Vérifiez que le workflow passe au vert dans l’onglet **Actions**

---

## Livrables

1. Lien vers le repository GitHub
2. Fichier `.github/workflows/mlops-pipeline.yml`
3. Rapport court (1-2 pages) avec :
   - Captures d’écran (workflow vert + Model Registry en Staging)
   - Réponses aux 3 questions :
     1. Quels types de tests avez-vous implémentés et pourquoi ?
     2. Pourquoi la promotion vers Production ne doit-elle pas être automatique ?
     3. Quels guardrails supplémentaires ajouteriez-vous en contexte industriel (AI Act, banque, santé…) ?

---

## Aide rapide

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError: src` | Lancez les commandes depuis la racine du projet |
| MLflow Connection refused | Vérifiez que `mlflow server` tourne |
| Accuracy trop faible | Dataset très petit → normal. Le seuil est volontairement bas (0.6) |
| Workflow GitHub rouge | Regardez les logs dans l’onglet Actions |

Bon TP !

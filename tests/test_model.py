from src.train import train


def test_model_accuracy_threshold():
    model, metrics = train()
    assert metrics["accuracy"] >= 0.6, f"Accuracy trop faible : {metrics['accuracy']:.2f}"
    assert metrics["f1"] >= 0.5, f"F1 trop faible : {metrics['f1']:.2f}"


def test_model_can_predict():
    model, _ = train()
    pred = model.predict(["Ce produit est vraiment super"])
    assert pred[0] in [0, 1]

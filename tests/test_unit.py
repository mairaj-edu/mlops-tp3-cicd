from src.data import load_params, load_data
from src.model import build_model


def test_load_params():
    params = load_params()
    assert "data" in params
    assert "model" in params
    assert params["data"]["test_size"] == 0.2


def test_load_data():
    df = load_data()
    assert len(df) >= 10
    assert "text" in df.columns
    assert "label" in df.columns


def test_build_model():
    params = load_params()
    model = build_model(params)
    assert model is not None
    assert hasattr(model, "fit")

from src.data import load_data


def test_no_missing_values():
    df = load_data()
    assert df.isnull().sum().sum() == 0, "Des valeurs manquantes sont présentes"


def test_label_values():
    df = load_data()
    assert set(df["label"].unique()).issubset({0, 1})


def test_text_not_empty():
    df = load_data()
    assert (df["text"].str.strip() != "").all()


def test_minimum_samples():
    df = load_data()
    assert len(df) >= 10, "Le dataset est trop petit"

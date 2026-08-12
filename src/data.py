import pandas as pd
from sklearn.model_selection import train_test_split
import yaml


def load_params(path="params.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def load_data(path="data/reviews.csv"):
    df = pd.read_csv(path)
    return df


def split_data(df, params):
    X = df["text"]
    y = df["label"]
    return train_test_split(
        X, y,
        test_size=params["data"]["test_size"],
        random_state=params["data"]["random_state"],
        stratify=y
    )

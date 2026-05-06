import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df = df.copy()

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")

    df = df.dropna(subset=["type", "title", "release_year"])

    return df

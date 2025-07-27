import pandas as pd


def load_historical_df(path="data/raw/historical_btc_2018.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()
    df["date"] = pd.to_datetime(df["date"])
    df.to_csv("data/transformed/transormed_data.csv", index=False)
    return df

import pandas as pd


def load_historical_csv(path="data/raw/historical_btc_2018.csv"):
    df = pd.read_csv(path)
    return df


load_historical_csv()

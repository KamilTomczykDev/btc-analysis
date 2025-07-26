def clean_crypto_df(df):
    df = df.copy()
    df = df.dropna()
    df = df.sort_values(by="market_cap", ascending=False)
    return df

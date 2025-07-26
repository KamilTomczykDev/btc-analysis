from src.extract_api import fetch_current_crypto_data
from src.extract_csv import load_historical_df
from src.transform import clean_crypto_df
from src.load import load_to_sqlite

# ETL api
df_api = fetch_current_crypto_data()
df_api = clean_crypto_df(df_api)
load_to_sqlite(df_api, table_name="crypto_prices")

# ETL csv

df_csv = load_historical_df()
load_to_sqlite(df_csv, table_name="historical_df")

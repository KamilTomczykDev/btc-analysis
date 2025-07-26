import sqlite3


def load_to_sqlite(df, table_name="crypto_prices", db_path="db/crypto_data.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="append", index=False)
    conn.close()

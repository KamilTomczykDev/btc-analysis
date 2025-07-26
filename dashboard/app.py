import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

DB_PATH = "db/crypto_data.db"

# -----------------------------
# Funkcje pomocnicze
# -----------------------------


@st.cache_data
def load_current_crypto_data():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT *
        FROM crypto_prices
        ORDER BY timestamp DESC
        LIMIT 50
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


@st.cache_data
def load_historical_btc():
    df = pd.read_csv("data/raw/historical_btc_2018.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


# -----------------------------
# UI – Streamlit layout
# -----------------------------

st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("📊 Crypto Dashboard – Aktualne dane vs. Historia BTC (2018)")

# Załaduj dane
crypto_df = load_current_crypto_data()
btc_df = load_historical_btc()

# Top 5 coinów
top5 = (
    crypto_df.sort_values("market_cap", ascending=False)
    .drop_duplicates("symbol")
    .head(5)
)

# -----------------------------
# Sekcja: Tabela top 5 coinów
# -----------------------------
st.subheader("🔝 Top 5 kryptowalut (na podstawie market cap)")

st.dataframe(
    top5[["symbol", "current_price", "market_cap", "price_change_percentage_24h"]],
    use_container_width=True,
)

# -----------------------------
# Sekcja: Wykres BTC historyczny
# -----------------------------
st.subheader("📈 Wykres historyczny ceny BTC (2018)")

fig = px.line(btc_df, x="Date", y="BTC Price (USD)", title="BTC – cena w 2018 roku")
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Sekcja: Porównanie procentowe (opcjonalne)
# -----------------------------
st.subheader("📉 Porównanie: dzienna zmiana top coinów")

bar_fig = px.bar(
    top5,
    x="symbol",
    y="price_change_percentage_24h",
    title="Dzienna zmiana ceny (%) – top 5 coinów",
    color="price_change_percentage_24h",
    color_continuous_scale="RdYlGn",
)
st.plotly_chart(bar_fig, use_container_width=True)

st.caption(
    "Dane aktualne z CoinGecko API (via lokalna baza danych). Dane historyczne BTC pochodzą z pliku CSV."
)

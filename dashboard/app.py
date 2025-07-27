import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st

DB_PATH = "db/crypto_data.db"


# Helper functions
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


# UI – Streamlit layout
st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("📊 Crypto Dashboard – Live Data vs Historical BTC (2018)")

# Load data
crypto_df = load_current_crypto_data()
btc_df = load_historical_btc()

# Top 5 coins
top5 = (
    crypto_df.sort_values("market_cap", ascending=False)
    .drop_duplicates("symbol")
    .head(5)
)

# Top 5 coins table
st.subheader("🔝 Top 5 Cryptocurrencies (by Market Cap)")

st.dataframe(
    top5[["symbol", "current_price", "market_cap", "price_change_percentage_24h"]],
    use_container_width=True,
)

# BTC historical chart
st.subheader("📈 BTC Price Chart (2018)")

fig = px.line(btc_df, x="Date", y="BTC Price (USD)", title="BTC Price in 2018")
st.plotly_chart(fig, use_container_width=True)


# Daily price change
st.subheader("📉 Daily Price Change – Top 5 Coins")

bar_fig = px.bar(
    top5,
    x="symbol",
    y="price_change_percentage_24h",
    title="24h Price Change (%) – Top 5 Coins",
    color="price_change_percentage_24h",
    color_continuous_scale="RdYlGn",
)
st.plotly_chart(bar_fig, use_container_width=True)

st.caption(
    "Live data sourced from CoinGecko API (via local database). BTC historical data loaded from CSV file."
)

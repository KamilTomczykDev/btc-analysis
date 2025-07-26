import requests
import pandas as pd
from datetime import datetime


def fetch_current_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10}
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)[
        ["id", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]
    ]
    df["timestamp"] = datetime.utcnow()
    return df

import requests
import pandas as pd
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

# =========================
# FACT TABLE
# =========================
f_crypto = df[[
    "id",
    "current_price",
    "market_cap",
    "total_volume",
    "price_change_percentage_24h"
]].copy()

f_crypto["date"] = datetime.now()

f_crypto.columns = [
    "coin_id",
    "price",
    "market_cap",
    "volume",
    "price_change_24h",
    "date"
]

# =========================
# DIM COIN TABLE
# =========================
d_coin = df[[
    "id",
    "name",
    "symbol"
]].drop_duplicates()

d_coin.columns = [
    "coin_id",
    "name",
    "symbol"
]

# Output all tables
f_crypto, d_coin

import requests
import pandas as pd

base = "https://testnet.binancefuture.com"
path = "/fapi/v1/klines"
url = base + path
param = {"symbol": "XRPUSDT", "interval": "1h", "limimit": 10}

def price_check(df):
    max_value = max(df['Price'])
    min_value = min(df['Price'])
    if min_value/max_value < 0.99:
        print("Alert")

while True:
    r = requests.get(url, params=param)
    if r.status_code == 200:
        data = pd.DataFrame(r.json())
        print(data)
    else:
        print("Error")
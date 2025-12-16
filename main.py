import datetime

now = datetime.datetime.utcnow()
print("Hello GitHub Actions!")
print("Current UTC time:", now)

import os

api_key = os.getenv("BINANCE_API_KEY")
secret = os.getenv("BINANCE_SECRET")

print("BINANCE_API_KEY loaded:", bool(api_key))
print("BINANCE_SECRET loaded:", bool(secret))

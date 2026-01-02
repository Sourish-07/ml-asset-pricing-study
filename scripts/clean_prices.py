import pandas as pd

prices = pd.read_csv("data/processed/prices_all.csv")

prices.columns = [c.lower() for c in prices.columns]

expected = {"date", "open", "high", "low", "close", "volume", "symbol"}
missing = expected - set(prices.columns)

if missing:
    raise ValueError(f"Missing columns: {missing}")

prices["date"] = pd.to_datetime(prices["date"])

prices = prices[prices["volume"] > 0]

prices = prices.sort_values(["symbol", "date"])

prices.to_csv("data/processed/prices_clean.csv", index=False)

print("Saved prices_clean.csv")
print("Shape:", prices.shape)

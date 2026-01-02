import pandas as pd

prices = pd.read_csv("data/processed/prices_clean.csv")
prices["date"] = pd.to_datetime(prices["date"])

prices["return_1d"] = (
    prices.groupby("symbol")["close"]
    .pct_change()
)

prices = prices.dropna(subset=["return_1d"])

prices.to_csv("data/processed/returns_panel.csv", index=False)

print("Saved returns_panel.csv")
print("Shape:", prices.shape)

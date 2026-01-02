import pandas as pd
from pathlib import Path

price_dir = Path("data/raw/prices/stocks")

print("Looking for price files in:", price_dir.resolve())

files = list(price_dir.glob("*.txt"))
print("Number of .txt files found:", len(files))

frames = []
skipped = 0

for file in files:
    try:
        df = pd.read_csv(file)

        if df.empty or len(df.columns) == 0:
            skipped += 1
            continue

        symbol = file.stem
        df["Symbol"] = symbol
        frames.append(df)

    except Exception as e:
        skipped += 1
        continue

print("Skipped files:", skipped)

if not frames:
    raise RuntimeError("No valid price files loaded.")

prices = pd.concat(frames, ignore_index=True)

prices.to_csv("data/processed/prices_all.csv", index=False)

print("Saved prices_all.csv")
print("Final shape:", prices.shape)

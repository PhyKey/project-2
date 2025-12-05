import pandas as pd
from pathlib import Path

CLEAN_DIR = Path("src/data/clean")
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

def analyze():
    df = pd.read_csv(CLEAN_DIR / "cleaned_weather.csv", parse_dates=["timestamps"])
    summary = {
        "min_temperature" : df["temperature"].min(),
        "max_temperature" : df["temperature"].max(),
        "avg_temperature" : df["temperature"].mean(),
        "total_precipitation" : df["precipitation"].sum(),
    }
    print("Weather Data Summary:")
    for k, v in summary.items():
        print(f"{k}: {v}")
    return summary

if __name__ == "__main__":
    analyze()
import json
import pandas as pd
from pathlib import Path

RAW_DIR = Path("src/data/raw")
CLEAN_DIR = Path("src/data/clean")
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

def load_latest_raw_file():
    """ Load the latest raw data file from data/raw directory."""
    raw_file = sorted(RAW_DIR.glob("weather_*.json"))
    if not raw_file:
        raise FileNotFoundError("No raw data files found in data/raw directory.")
    return raw_file[-1]

def clean_weather(raw_file: Path):
    """ raw_file: Path to the raw JSON file.
        return DataFrame with cleaned weather data. """
    with raw_file.open(encoding="utf-8") as f:
        data = json.load(f)
        hourly = data.get("hourly", {})
        timestamps = hourly.get("time", [])
        temperatures = hourly.get("temperature_2m", [])
        rain = hourly.get("precipitation", [])

        # Sanity check
        if not timestamps:
            raise ValueError("No timestamps found in the raw data.")
        
        df = pd.DataFrame({
            "timestamps" : pd.to_datetime(timestamps),
            "temperature": temperatures,
            "precipitation" : rain,
        })

        # Sort by datetime
        df = df.sort_values(by="timestamps").reset_index(drop=True)
        return df
    
def save_cleaned_data(df: pd.DataFrame):
    out_csv = CLEAN_DIR / "cleaned_weather.csv"
    df.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"Saved cleaned data to {out_csv}")
    return out_csv

if __name__ == "__main__":
    newest = load_latest_raw_file()
    df = clean_weather(newest)
    save_cleaned_data(df)
    print(df.sample(10))
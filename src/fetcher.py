import requests
from pathlib import Path
import datetime
import json
import sys
import time

DATA_DIR = Path("src/data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_LAT = 34.69 # Osaka
DEFAULT_LON = 135.51 # Osaka

def fetch_weather(lat=DEFAULT_LAT, lon=DEFAULT_LON):
    """ Fetch weather data from Open-Meteo and save to data/raw with timestamped filename. """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation",
        "timezone": "Asia/Tokyo"
    }
    attempt = 0
    while attempt < 3:
        try:
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()
            parsed = r.json()
            now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H%M%SZ")
            filename = DATA_DIR / f"weather_{lat}_{lon}_{now}.json"
            filename.write_text(json.dumps(parsed, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"Saved weather data to {filename}")
            return parsed
        except Exception as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}", file=sys.stderr)
            if attempt < 3:
                time.sleep(2 * attempt)
            else:
                raise

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
        fetch_weather(lat, lon)
    else:
        fetch_weather()
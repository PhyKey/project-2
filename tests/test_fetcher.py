from src import fetcher
import pathlib
import json

def test_fetch_weather(tmp_path):
    # Use a temporary directory for data storage
    fetcher.DATA_DIR = pathlib.Path(tmp_path)
    parsed = fetcher.fetch_weather()
    assert isinstance(parsed, dict)
    assert "hourly" in parsed
    files = list(pathlib.Path(tmp_path).glob("weather_*.json"))
    assert len(files) == 1
    content = json.loads(files[0].read_text(encoding="utf-8"))
    assert 'hourly' in content
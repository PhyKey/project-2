from src.fetcher import fetch_weather
from src.cleaner import clean_weather, save_cleaned_data, load_latest_raw_file
from src.analyzer import analyze
from src.report_generator import generate_report
from src.email_sender import send_report
import os

def main():
    print("1. Fetching weather data...")
    raw = fetch_weather()

    print("\n2. Cleaning weather data...")
    raw_file = load_latest_raw_file()
    df = clean_weather(raw_file)
    save_cleaned_data(df)

    print("\n3. Analyzing weather data...")
    analyze()

    print("\n4. Generating report...")
    generate_report()

    print("\n5. Sending report via email...")
    if os.getenv("EMAIL_USER") and os.getenv("EMAIL_PASS"):
        try:
            send_report("reports/weekly_weather_report.pdf")
        except Exception as e:
            print(f"Email send failed: {e}")
    else:
        print("Skipping email (EMAIL_USER/EMAIL_PASS not set)")
    print("\nAll tasks completed.")

if __name__ == "__main__":
    main()
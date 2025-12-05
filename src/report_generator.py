import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

CLEAN_DIR = Path("src/data/clean")
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

def load_chart_data():
    df = pd.read_csv(CLEAN_DIR / "cleaned_weather.csv", parse_dates=["timestamps"])
    return df

def create_chart(df):
    chart_path = REPORT_DIR / "weekly_temperature_chart.png"
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamps"], df["temperature"], label="Temperature (°C)", color='blue')
    plt.title("Weekly Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def create_excel(df, summary):
    excel_path = REPORT_DIR / "weekly_weather_report.xlsx"
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Raw Data")
        pd.DataFrame([summary]).to_excel(writer, index=False, sheet_name="Summary")
    return excel_path

def create_pdf(chart_path, summary):
    pdf_path = REPORT_DIR / "weekly_weather_report.pdf"
    doc = SimpleDocTemplate(str(pdf_path))
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph("Weekly Weather Report", styles["Title"]))
    story.append(Spacer(1, 12))
    for k, v in summary.items():
        story.append(Paragraph(f"{k}: {v}", styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Image(str(chart_path), width=500, height=200))
    doc.build(story)
    return pdf_path

def analyze_summary(df):
    return {
        "min_temperature" : df["temperature"].min(),
        "max_temperature" : df["temperature"].max(),
        "avg_temperature" : round(df["temperature"].mean(), 2),
        "total_precipitation" : df["precipitation"].sum()
    }

def generate_report():
    df = load_chart_data()
    summary = analyze_summary(df)
    chart_path = create_chart(df)
    excel_path = create_excel(df, summary)
    pdf_path = create_pdf(chart_path, summary)
    print(f"Generated report:")
    print(f"- Chart: {chart_path}")
    print(f"- Excel: {excel_path}")
    print(f"- PDF: {pdf_path}")

if __name__ == "__main__":
    generate_report()
# Automated Web Scraper & Weekly Report System  
An end-to-end Python automation that scrapes data, cleans it, analyzes trends, generates a weekly PDF report, and emails it automatically. 

## Features

### **1. Web Scraping**
- Scrapes data from a target website/API
- Captures raw HTML data
- Stores results with timestamps for reproducibility

### **2. Data Cleaning**
- Converts raw scraped HTML into structured data
- Handles missing fields, strange formats, duplicates, etc.
- Outputs clean, analysis-ready DataFrame

### **3. Analysis**
- Weekly summary (min, max, average, trends)
- Detects changes from previous periods
- Provides insights used in reports

### **4. Automated PDF Report**
- Generates a clean PDF with:
  - Summary table  
  - Trend insights  
  - Timestamp  
- Stored in `/reports/xxxx.pdf`

### **5. Email Automation**
- Sends the weekly PDF report automatically to your email  
- Uses secure app passwords + SMTP with SSL  
- 100% automated, ready for cron / cloud scheduler

### **6. Modular Pipeline (Single Entry)**
One command runs the whole flow:

```bash
python run_all.py

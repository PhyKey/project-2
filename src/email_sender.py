import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_report(pdf_path):
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    email_to = email_user
    msg = EmailMessage()
    msg['Subject'] = "Weekly Weather Report"
    msg['From'] = email_user
    msg['To'] = email_to
    msg.set_content("Here is the automated weekly weather report.")
    with open(pdf_path, 'rb') as f:
        file_data = f.read()
        file_name = pdf_path.split("/")[-1]
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_user, email_pass)
        smtp.send_message(msg)
    print(f"Email sent to {email_to} with attachment {file_name} successfully.")
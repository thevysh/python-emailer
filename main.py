import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

def send_plain_email(to_address: str, subject: str, body: str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"Plain text email sent to {to_address}!")

def send_html_email():
    msg = EmailMessage()
    msg['Subject'] = 'HTML Email from Python'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with open('templates/welcome.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    msg.add_alternative(html_content, subtype='html')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("HTML email sent!")

if __name__ == "__main__":
    send_plain_email()
    send_html_email()

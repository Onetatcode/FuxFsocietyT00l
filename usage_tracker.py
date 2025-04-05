import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime

# Using environment variables to hide sensitive info
def notify():
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    email_password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEText(f"Tool used on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    msg["Subject"] = "Fsociety Tool Usage"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, email_password)
        server.send_message(msg)

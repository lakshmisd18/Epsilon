import smtplib
from email.mime.text import MIMEText

def send_email(
    receiver_email,
    subject,
    message
):

    sender_email = "lakshmisd2005@gmail.com"

    app_password = "lvzzwpmnphhufard"

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        server.send_message(msg)
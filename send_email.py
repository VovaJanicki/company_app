import os
import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "yavb.if@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "yavb@wp.pl"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# send_email()

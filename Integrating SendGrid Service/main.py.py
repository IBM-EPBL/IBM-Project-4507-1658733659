import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


def send_email():
    from_email = Email('suryaprasath.j2019ece@sece.ac.in')
    to_email = To('j.suryaprasath18@gmail.com')
    subject = 'Sending with SendGrid is Fun'
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, content)

    try:
        sg = SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


send_email()
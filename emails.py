#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generate_email(From, To, subject, body, attachment=""):
    # set message content
    message = EmailMessage()
    message['From'] = From
    message['To'] = To 
    message['Subject'] = subject
    message.set_content(body)

    # set attachment
    if attachment:
        attachment_path = attachment
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'r') as ap:
            message.add_attachment(ap.read(),maintype=mime_type, subtype=mime_subtype,filename=os.path.basename(attachment_path))
    return message

def send_email(email):
    mail_server = smtplib.SMTP("smtp.gmail.com")
    mail_server.send_message(email)
    mail_server.quit()
#!/usr/bin/env python3

import psutil
import emails 
import os 
import time
import socket

def health_check():
    subject = ""
    if psutil.cpu_percent() > 80:
        subject = "Error - CPU usage is over 80%"
    elif psutil.disk_usage('/').percent < 20:
            subject = "Error - Available disk space is less than 20%"
    elif psutil.virtual_memory().free / (1024.0 ** 2) < 500:
            subject = "Error - Available memory is less than 500MB"
    elif socket.gethostbyname('localhost') != '127.0.0.1':
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    return subject

if __name__ == "__main__":
    From = "systemreport@localhost.com"
    To = os.environ.get('MyEmail') 
    body = "Please check your system and resolve the issue as soon as possible."
    while True:
        subject = health_check(subject)
        if subject:
            email = emails.generate_email(From, To, subject, body)
            emails.send_email(email)
        time.sleep(60)

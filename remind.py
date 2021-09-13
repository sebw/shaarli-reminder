#/usr/bin/env python3

import shaarli_client.client as c
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

shaarli_url = os.environ.get('SHAARLI_URL')
shaarli_api = os.environ.get('SHAARLI_API')
shaarli_tag = os.environ.get('SHAARLI_TAG')
smtp_sender = os.environ.get('SMTP_SENDER')
smtp_recipient = os.environ.get('SMTP_RECIPIENT')
smtp_server = os.environ.get('SMTP_SERVER')
smtp_port = os.environ.get('SMTP_PORT')
smtp_password = os.environ.get('SMTP_PASSWORD')
smtp_username = os.environ.get('SMTP_USERNAME')

response = c.ShaarliV1Client(shaarli_url, shaarli_api)
answer = response.get_links({'searchtags': shaarli_tag, 'limit': 'all'})

j = answer.text
a = json.loads(j)

smtp_body=[]
smtp_body.append("---")
for i in a:
    smtp_body.append(i['title'])
    smtp_body.append(i['url'])
    smtp_body.append("---")

multiline_body = "\n".join(smtp_body)

msg = MIMEMultipart()

msg['From'] = smtp_sender
msg['To'] = smtp_recipient
msg['Subject'] = 'Your Shaarli Bookmark Reminder for tag "' + str(shaarli_tag) + '"'
msg.attach(MIMEText(multiline_body))

server = smtplib.SMTP(smtp_server + ":" + str(smtp_port))
server.ehlo()
server.starttls()
server.ehlo()
server.login(smtp_sender, smtp_password)
server.sendmail(smtp_sender,smtp_recipient,msg.as_string())
server.quit()
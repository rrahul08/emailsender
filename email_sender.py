import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'rahulr1805@outlook.com'
email['to'] = 'rahulvirat655@gmail.com'
email['subject'] = 'Hi !'

email.set_content(html.substitute({'name':'Virat'}),'html')

with smtplib.SMTP(host='smtp.outlook.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('rahulr1805@outlook.com','awmm416@R')
    smtp.send_message(email)
    print('All good!')
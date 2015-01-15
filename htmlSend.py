from smtplib import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

server = SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
print 'server recognized'

from_id = ''
rec_id = ''
pwd=''

body=''
subject=''
message=''
msg = MIMEMultipart('alternative')

from_id = raw_input("Enter your id --> ")
pwd = raw_input("Enter pwd")
server.login(from_id,pwd)

rec_id = raw_input("Enter recievers id --> ")
subject = raw_input("Enter subject --> ")
body = raw_input("Enter body --> ")

html_text = "<h1>Subject --> <br>"+subject+"</h1>"
html_text += "<h2>Body --> <br>"+body+"</h2>"

msg['Subject'] = subject
msg['From'] = from_id
msg['To'] = rec_id
msg.attach(MIMEText(html_text,'html'))



server.sendmail(from_id,rec_id,msg.as_string())
print 'send'
server.quit()

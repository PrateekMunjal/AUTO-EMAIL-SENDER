from smtplib import *
from getpass import *
from re import *
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
from tkFileDialog import *

#Server Setup
server = SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
to = 'munjalprateek31@gmail.com'
from_id = raw_input('Enter sender\'s id : ')
password = getpass('Enter password : ')
server.login(from_id,password)
server.ehlo()

msg = MIMEMultipart()

#Enter subject
sub = raw_input('Enter Subject : ')
msg['Subject']=sub
msg['From']=from_id
msg['To']=to

path = askopenfilename()
if(path!=''):
    extension = path.split('.')[1]
    FileName = (path[::-1].split('/')[0])[::-1]
    ref = open(path).read()
    attachment = MIMEApplication(ref,_subtype=extension)
    attachment.add_header('content-disposition','attachment',filename=FileName)
    msg.attach(attachment)
    print '%s Attached Successfully'%FileName

server.sendmail(from_id,[to],msg.as_string())
print 'Successfully Sent'
server.close()


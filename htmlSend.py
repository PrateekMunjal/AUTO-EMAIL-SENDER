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


html_text = """
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
<center>
  <div style="width:600px;margin:auto">
    <div style="background-color:#006cb5;margin-top:20px;padding:10px;color:white;font-family:helvetica;font-size:15px">
     Subject :  
      <i>
        <!-- here comes the subject -->"""+subject+"""
      </i>
    </div>
<div style="background-color:#006cb5;margin-top:20px;padding:10px;color:white;font-family:helvetica;font-size:15px">
     Bleedred 
      <i>
        - Web Application
      </i>
      ;)
    </div>
    <div style="background-color:#f4f4f4;padding:10px;border:1pt solid #eee">
      <a href="http://www.bleedred.org" style="text-decoration:none!important" target="_blank">
        <div style="background-color:white;border:1pt solid #d3d3d3;padding:5px">
          <table style="font-family:helvetica;font-size:13px;border-collapse:collapse" width="100%" border="0">
            <tbody>
              <tr>
                <td colspan="3" style="font-weight:bold;line-height:20px;color:black" align="left">
                  Visit Application
                </td>
              </tr>
              <tr>
                <td colspan="3" style="color:#006cb5;line-height:16px" align="left">
                  <span style="font-weight:bold">
                    Bleedred
                  </span>
                  (An Application to use in emergency)
                </td>

              </tr>
              <tr>
                <td colspan="3">
                  <hr width="564" color="#ddd" align="center" size="1" style="margin:5px 0 2px 0">
                </td>
              </tr>
              
            </tbody>

		
          </table>
        </div>
      </a>
<a href="https://www.facebook.com/Blood.App.HelpingWorld" style="text-decoration:none!important" target="_blank">
        <div style="background-color:white;border:1pt solid #d3d3d3;padding:5px">
          <table style="font-family:helvetica;font-size:13px;border-collapse:collapse" width="100%" border="0">
            <tbody>
              <tr>
                <td colspan="3" style="font-weight:bold;line-height:20px;color:black" align="left">
                  Visit Facebook Page
                </td>
              </tr>
              <tr>
                <td colspan="3" style="color:#006cb5;line-height:16px" align="left">
                  <span style="font-weight:bold">
                    Bleedred
                  </span>
                  (An Application to use in emergency)
                </td>
              </tr>
              <tr>
                <td colspan="3">
                  <hr width="564" color="#ddd" align="center" size="1" style="margin:5px 0 2px 0">
                </td>
              </tr>
              
            </tbody>
		
          </table>
        </div>
<div style="background-color:white;border:1pt solid #d3d3d3;padding:5px">
          <table style="font-family:helvetica;font-size:13px;border-collapse:collapse" width="100%" border="0">
            <tbody>
              <tr>
                <td colspan="3" style="font-weight:bold;line-height:20px;color:black" align="left">
                  Body
                </td>
              </tr>
              <tr>
                <td colspan="3" style="color:#006cb5;line-height:16px" align="left">
                  <span style="font-weight:bold">
                  """+body+"""
                    <!-- here comes the body -->
                  </span>
                </td>
              </tr>
              <tr>
                <td colspan="3">
                  <hr width="564" color="#ddd" align="center" size="1" style="margin:5px 0 2px 0">
                </td>
              </tr>
              
            </tbody>
		
          </table>
        </div>
      </a>
    </div>
  </div>
</center>
</body>
</html>
"""
msg['Subject'] = subject
msg['From'] = from_id
msg['To'] = rec_id
msg.attach(MIMEText(html_text,'html'))



server.sendmail(from_id,rec_id,msg.as_string())
print 'send'
server.quit()

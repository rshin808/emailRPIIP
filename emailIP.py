import smtplib
import os
import time

from email.mime.text import MIMEText

time.sleep(30)

fileIP = "IPADDRESS.txt"
os.system("ifconfig > IPADDRESS.txt")

fp = open(fileIP, "rb")

msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = "RPI IP ADDRESS"
msg['From'] = "from"
msg['To'] = "to"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login('usr', 'pd')
s.sendmail("from", "to", msg.as_string())
s.quit()

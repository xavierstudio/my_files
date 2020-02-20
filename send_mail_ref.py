#!/usr/bin/env python3
# coding=utf-8
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('hello，send by python_test...','plain','utf-8')
sender = 'sender@163.com'
password = 'xxxxx'

receiver = 'receiver@qq.com'
mailto_list = ['AAA@163.com','BBB@qq.com']

smtp_server = 'smtp.163.com'
msg['From'] = sender
msg['To'] =';'.join(mailto_list)
msg['Subject'] = 'from IMYalost'

server = smtplib.SMTP(smtp_server,25)
server.login(sender,password)
server.set_debuglevel(1)
server.sendmail(sender,mailto_list,msg.as_string())
server.quit()

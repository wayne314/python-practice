#-*-coding:utf-8-*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import  smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),
                       addr.encode('utf-8') if isinstance(addr,unicode) else addr))
from_addr='wayne_314@163.com'
password='221Iloveyoudw*'
to_addr='x_flyman@163.com'
smtp_server='smtp.163.com'
msg=MIMEText('来此Python团的提示，人生苦短，我用Python!', 'plain','utf-8')
msg['From']=_format_addr(u'Python军团<%s>'%from_addr)
msg['To']=_format_addr(u'接收员<%s>'%to_addr)
msg['Subject']=Header(u'来自Python军团的SMTP问候……','utf-8').encode()
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
#from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '97***427@qq.com'
password = 'ipv***bbgg'
to_addr = '112****8856@qq.com'
smtp_server = 'smtp.qq.com'
html='''<html>
        	<body>
        	    <h1>Hello the fuck world</h1>
        	    <p>使用python发送邮件</p>
        	    <P><a href="https://www.cnblogs.com/lovealways/p/6701662.html">参考链接1 cnblogs</a><p>
        	    <P><a href="https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000">参考链接2 廖雪峰python教程</a><p>        	    
        	    <br />
        	    <br />
        	    <hr />
    			<p>Send By <a href="http://www.python.org">Python</a>...</p>
      		</body>
        </html>
    '''


msg = MIMEText(html, 'html', 'utf-8')
msg['From'] = _format_addr('Python <%s>' % from_addr)
msg['To'] = _format_addr('我自己 <%s>' % to_addr)
msg['Subject'] = Header('come form SMTP test....', 'utf-8').encode()

try:
	#server = smtplib.SMTP(smtp_server, 465),这两句不行
	#server.starttls()
	server = smtplib.SMTP_SSL(smtp_server,465)
	server.set_debuglevel(1)
	server = smtplib.SMTP_SSL(smtp_server,465)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	print('发送成功')
except Exception:
    print ("发送失败")
finally:
	server.quit()


'''
#SMTP发送qq邮件
#coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg_from='97****27@qq.com'          #发送方邮箱
passwd='ipvr****lfxbbgg'                 #填入发送方邮箱的授权码
msg_to='112****56@qq.com'             #收件人邮箱
                            
subject="python mail test"               #主题     
content="hello python"

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except s.SMTPException as e:
    print ("发送失败")
finally:
    s.quit()

'''
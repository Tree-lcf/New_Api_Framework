# -*- coding:utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


class SendMail:

    def __init__(self):
        self.from_addr = "."
        self.smtp_server = 'smtp.163.com'
        self.password = ''

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_msg(self, msg_content, to_addr, subject):
        msg = MIMEText(msg_content, 'plain', 'utf-8')
        msg['From'] = self._format_addr('Test Center <%s>' % self.from_addr)
        msg['To'] = self._format_addr('App项目组 <%s>' % to_addr)
        msg['Subject'] = Header(subject, 'utf-8').encode()
        server = smtplib.SMTP(self.smtp_server, 25)
        # server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, to_addr, msg.as_string())
        server.quit()

    def send_main(self, pass_list, fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        total_num = pass_num + fail_num
        to_addr_list = ['16681256@qq.com']
        subject = '接口自动化测试报告'
        content = "本次运行总共:[%d]个接口用例,通过个数:[%d],失败个数:[%d]" % (total_num, pass_num, fail_num)
        self.send_msg(content, to_addr_list, subject)

'''
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
'''
if __name__ == "__main__":
    sendmail = SendMail()
    sendmail.send_main(['正常登录', '正常获取商品最新价格', '正常获取商品价格趋势', '正常获取商品历史价格', '正常获取商品时间区间历史趋势'], [])

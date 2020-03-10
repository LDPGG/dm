# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 0023 上午 10:40
# @Author  : 刘登攀阿！！
# @FileName: setup.py.py
# @Software: PyCharm
'''
自动发送QQ邮件
'''
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header


def email_set():
    email_from = "@qq.com"  # 改为自己的发送邮箱
    email_to = "@qq.com"  # 接收邮箱
    hostname = ".qq.com"  # 不变，QQ邮箱的smtp服务器地址
    login = "@qq.com"  # 发送邮箱的用户名
    password = ""  # 发送邮箱的密码，即开启smtp服务得到的授权码。注：不是QQ密码。
    subject = "我爱你"  # 邮件主题
    text = "send email"  # 邮件正文内容

    smtp = SMTP_SSL(hostname)  # SMTP_SSL默认使用465端口
    smtp.login(login, password)

    msg = MIMEText(text, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["from"] = email_from
    msg["to"] = email_to

    smtp.sendmail(email_from, email_to, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    email_set()


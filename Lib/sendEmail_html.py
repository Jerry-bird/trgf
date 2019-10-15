# coding=utf-8

import unittest
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time


# ==============定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    username = 'log@wdtrgf.com.cn'  # 发件箱用户名
    password = '43ed$#ED'  # 发件箱密码
    sender = 'log@wdtrgf.com.cn'  # 发件人邮箱
    receiver = ['lipeng@wdtrgf.com.cn', 'test@wdtrgf.com.cn']  # 收件人邮箱
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()
    msg['From'] = Header(u'接口自动化测试 <%s>' % sender)
    # msg['To'] = Header(u'收件人 <%s>' % receiver)
    msg['To'] = ';'.join(receiver)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('218.76.8.40', '9125')  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_path = "C:\\Users\\lp403\\PycharmProjects\\trgf\\Report\\"
    new_report = new_report(test_path)
    send_mail(new_report)  # 发送测试报告

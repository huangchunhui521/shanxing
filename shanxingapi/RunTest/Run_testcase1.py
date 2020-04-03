# -*- coding: utf-8 -*-


from shanxingapi.RunTest import *
import datetime


# coding:utf-8
import unittest
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

testcase_dir = "D:\qiangxiandao\TestCase"
report_dir = "D:\qiangxiandao\TestReport"

# 发送邮件
def sendmail(sendfile):
    smtpserver = 'smtp.exmail.qq.com'
    user = 'chunhui.huang@yitaichang.cn '
    password = 'Huangchunhui520'
    sender = 'chunhui.huang@yitaichang.cn'+';'+'qianhao.peng@yitaichang.cn'
    receiver = 'chunhui.huang@yitaichang.cn'
    subject = '自动化测试报告'
    message=MIMEText("各位领导及同事，附件是小程序自动化测试报告，请注意查收！")

    attach = MIMEText(sendfile, 'base64', 'utf-8')

    attach['Content-Type'] = 'application/octet-stream'
    attach['Content-disposition'] = 'attachment; filename = "text.html" '  # 邮件上显示的附件名称

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From']=sender
    msgRoot['To'] = receiver
    msgRoot.attach(attach)
    msgRoot.attach(message)


    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


# 查找目录下最新生成的测试报告,返回最新报告的详细路径
def find_Report(TestReport):
    lists = os.listdir(TestReport)
    lists.sort(key=lambda fn: os.path.getmtime(TestReport + "\\" + fn))
    newfile = os.path.join(TestReport, lists[-1])
    f = open(newfile, 'rb')
    mailfile = f.read()  # 读取测试报告作为邮件正文
    f.close()

    print(mailfile)
    return mailfile


# 运行case，并生成测试报告
def run_case():
    nowtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H_%M_%S')
    result = br(unittest.defaultTestLoader.discover(testcase_dir, "TestCase_HomePages.py"))
    result.report(
        filename="i抢鲜到-安卓" + nowtime + '自动化测试报告',
        description='i抢鲜到-安卓UI自动化测试',
        report_dir=report_dir,
    )


if __name__ == '__main__':
    run_case()
    new_report = find_Report(report_dir)
    sendmail(new_report)




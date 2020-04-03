# -*- coding: utf-8 -*- 

# @File: functions
# @Time :  2019/7/3 16:08
# @Author : bin.wang
# @Detail : 公用方法 数据库，邮件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymysql
from shanxingapi import conf, log



class GetData(object):

    __doc__ = "数据库操作"

    def __init__(self):
        self.log = log
        self.conf = conf
        self.cursor = None
        self.connect = None

    def select_database(self, sql):
        connect = pymysql.connect(
            host=self.conf.get("db", "host"),
            port=int(self.conf.get("db", "port")),
            user=self.conf.get("db", "username"),
            passwd=self.conf.get("db", "password"),
            charset=self.conf.get("db", "charset"),
            cursorclass=pymysql.cursors.DictCursor
        )
        self.connect = connect
        self.cursor = self.connect.cursor()
        try:
            self.log.debug("执行SQL：%s" % sql)
            self.cursor.execute(sql)
            self.log.info("success")
        except Exception as msg:
            self.log.error("fail: %s" % msg)
            return False
        data = self.cursor.fetchall()
        if not data:
            return None
        return data

    def connect_close(self):
        if self.cursor and self.connect:
            self.cursor.close()
            self.connect.close()
            self.log.warning("close connect：success")
            return True
        else:
            self.log.warning("closed connect")
            return True

    def check_db(self):
        try:
            self.select_database("SHOW DATABASES")
            self.connect_close()
            self.log.info("connect success")
            return True
        except Exception as msg:
            self.log.error("connect error: %s" % msg)
            return False


class SendMail(object):

    __doc__ = "发送邮件"

    def __init__(self):
        self.log = log
        self.conf = conf
        self.username = conf.get("mail", "username")
        self.password = conf.get("mail", "password")
        self.smtp = smtplib.SMTP()

    def close(self):
        self.smtp.quit()

    def send_email(self, msg, msg_to, subject):
        """
        发送邮件
        :param msg: 内容
        :param msg_to: 接收人
        :param subject: 主题
        :return:
        """
        smtpserver = 'smtp.163.com'
        sender = "AuToMail <{}>".format(self.username)
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = sender.strip('"')
        msgRoot['To'] = ','.join(msg_to)
        msgText = MIMEText('{0}'.format(msg), 'html', 'utf-8')
        msgRoot.attach(msgText)
        i, j = 1, 1
        while True:
            try:
                self.smtp.connect(smtpserver)
                self.smtp.login(self.username, self.password)
                self.log.info("email login success")
            except Exception as msg:
                self.log.error("[%s]:email login error: %s" % (i, msg))
                if i < 3:
                    i += 1
                    continue
                else:
                    return 400
            try:
                self.smtp.sendmail(self.username, msgRoot['To'].split(','), msgRoot.as_string())
                self.log.debug("email send success!")
            except Exception as msg:
                self.log.error("[%s]:email login error: %s" % (i, msg))
                if j < 3:
                    j += 1
                    continue
                else:
                    return 401
            break
        return 200









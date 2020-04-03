# -*- coding: utf-8 -*- 

# @File: __init__.py
# @Time :  2019/6/25 10:39
# @Author : bin.wang
# @Detail :

from shanxingapi.common import logger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser
import requests
import pymysql
import smtplib
import time
import json
import platform
import sys
import os


# 初始化配置文件路径
conf_path = '/testFile/mainConfig' if platform.system() != 'Windows' else '\\testFile\mainConfig'
conf_file_path = os.path.abspath(os.path.dirname(__file__)) + conf_path
conf = configparser.RawConfigParser()
conf.read(filenames=conf_file_path, encoding='utf-8')

# 初始化logger
logger.__DEBUG__ = True
log = logger.Log(os.path.basename(__file__)).logger_stream()


__all__ = [
    'conf',
    'log',
    'MIMEMultipart',
    'MIMEText',
    'smtplib',
    'time',
    'json',
    'os',
    'sys',
    'requests',
    'pymysql'
]
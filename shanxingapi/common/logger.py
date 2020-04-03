# -*- coding: utf-8 -*-

# @Time : 2019-04-17 15:47 
# @Author : Wangbin
import platform
import os
import logging
import colorlog
from datetime import datetime

curPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
logPath = curPath + '/logs/' if platform.system() != 'Windows' else curPath + '\logs\\'

if not os.path.exists(logPath):
    os.makedirs(logPath)

log_name = logPath + datetime.strftime(datetime.now(), '%Y-%m') + '_.log'

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'yellow',
    'WARNING': 'green',
    'ERROR': 'red',
    'CRITICAL': 'red',
}

__DEBUG__ = True


class Log(object):

    __doc__ = "控制台写入和日志文件写入 分离"

    def __init__(self, logger_name):
        self.fh = logging.FileHandler(filename=log_name, mode='a', encoding='utf-8')
        self.sh = logging.StreamHandler()
        self.logger_fh = logging.getLogger("logger_file")
        self.logger_sh = logging.getLogger(logger_name)
        if __DEBUG__:
            self._SET_LEVEL = logging.DEBUG
        else:
            self._SET_LEVEL = logging.INFO
        self.formatters = colorlog.ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d] | %(message)s', "%Y-%m-%d %H:%M:%S", log_colors=log_colors_config)
        self.formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(filename)s:[line:%(lineno)d] | %(message)s', "%Y-%m-%d %H:%M:%S")

    def close_logger(self):
        """
        关闭logger，一般不用
        :return: None
        """
        self.logger_fh.removeHandler(self.sh)
        self.logger_sh.removeHandler(self.fh)
        self.fh.close()
        self.sh.close()

    def logger_stream(self):
        """
        :return: logger object, 返回一个控制台日志的logger
        """
        self.logger_sh.setLevel(self._SET_LEVEL)
        self.sh.setFormatter(self.formatters)
        self.logger_sh.addHandler(self.sh)
        self.logger_sh.propagate = False
        return self.logger_sh

    def logger_file(self):
        """
        :return: logger object, 返回一个写日志文件的logger
        """
        self.logger_fh.setLevel(self._SET_LEVEL)
        self.fh.setFormatter(self.formatter)
        self.logger_fh.addHandler(self.fh)
        self.logger_fh.propagate = False
        return self.logger_fh


class Logger(object):

    __doc__ = "控制台和日志同时写入"

    def __init__(self, name):
        self.fh = logging.FileHandler(filename=log_name, mode='a', encoding='utf-8')
        self.sh = logging.StreamHandler()
        self.logger = logging.getLogger(name=name)
        if __DEBUG__:
            self._SET_LEVEL = logging.DEBUG
        else:
            self._SET_LEVEL = logging.INFO
        self.formatters = colorlog.ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d] | %(message)s', "%Y-%m-%d %H:%M:%S", log_colors=log_colors_config)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:[line:%(lineno)d] | %(message)s', "%Y-%m-%d %H:%M:%S")
        self.sh.setFormatter(self.formatters)
        self.fh.setFormatter(self.formatter)
        self.logger.setLevel(self._SET_LEVEL)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)
        self.logger.propagate = False

    def close_logger(self):
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)
        self.fh.close()
        self.sh.close()

    def log(self):
        return self.logger


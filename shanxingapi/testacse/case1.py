# -*- coding: utf-8 -*-
# @File:
# @Time :
# @Author :
# @Detail :



import unittest

from shanxingapi.testFile import fux_api
from shanxingapi.testFile.fux_api import Consumer


class ConsumerTestCase(unittest.TestCase):

    __doc__ = "TestCase"

    _classSetupFailed = True

    _cookies = None

    _shop_id = None

    _user_id = None

    _log = None

    _consumer = None

    @classmethod
    def setUpClass(cls):
        cls.consumer_object =fux_api.Consumer()
        cls._log = fux_api.log
        cls._log.debug("=" * 20)
        cls._log.debug("开始测试")

    @classmethod
    def tearDownClass(cls):
        cls._log.debug("="*20)
        cls._log.debug("结束测试")


    # def test_001(self):
    #     """礼物列表"""
    #     self.ret=Consumer().Master_list()
    #     self._log.info('```````{}'.format(self.ret))
    #     self.assertEqual(self.ret["code"], 0)


    # def test_002(self):
    #     """法师登录验证码授权"""
    #     ret=self.consumer_object.grant_authorization(phone='15818650805',code='123456')
    #     self.assertEqual(ret["code"], 0)


    def test_003(self):
        """法师登录接口"""
        # 获取法师登录验证码授权
        self.consumer_object.grant_authorization(phone='15818650805', code='11')
        # 法师端登录
        ret=self.consumer_object.login_Master(phone='15818650805')
        self.assertEqual(ret["code"], 0)


    def test_003(self):
        """法师登录接口"""
        # 获取法师登录验证码授权
        self.consumer_object.grant_authorization(phone='15818650805', code='11')
        # 法师端登录
        ret=self.consumer_object.login_Master(phone='15818650805')
        self.assertEqual(ret["code"], 0)



if __name__ == '__main__':
    unittest.main()
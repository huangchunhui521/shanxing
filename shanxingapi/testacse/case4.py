import unittest
import requests
import json

from shanxingapi import conf


class case1(unittest.TestCase):
    def setUp(self):
        # 法师列表的url

        self.host = conf.get("Master", "host")
        print(self.host)
        self.url = self.host + conf.get("Master", "Gift_list")
        print('url:'+self.url)



    def tearDown(self):
        print('执行结束')


    def test1(self):
        """法师列表"""
        pass


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行


from shanxingapi import *


try:
    conf.get("Master", "host")
except Exception as msg:
    log.error("请检查配置文件是否正确:%s" % msg)



class Consumer(object):

    def __init__(self):
        self.ret = None
        self.host = conf.get("Master", "host")
        self.userId = None
        self.cookies = None
        self.token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWYiOjE1ODc1NTEyNDgsIlRlbXBsZVVzZXIiOnsiaWQiOjI1OCwidXNlcl9pZCI6NTMzLCJ0ZW1wbGVfaWQiOjYxLCJjcmVhdGVkX2F0IjoiMjAxOS0xMS0yNiAxMToxNToyOCIsInVwZGF0ZWRfYXQiOiIyMDE5LTEyLTI3IDE3OjA0OjM3IiwidXBkYXRlX3VzZXJfbmFtZSI6MSwidXBkYXRlX2F2YXRhciI6MSwibmlja19uYW1lIjoi6YeK5byA5ouJIiwicGFzc3dvcmQiOiIkMnkkMTAkQTJjRjEvdXp3MVAwUG9VblpzaEtZdWJUbmRBVWZqUDZERy55c1RUbnhkR1dxazkwYTlvYzYiLCJhdmF0YXIiOiIvZ3JvdXAxL2RlZmF1bHQvMjAxOTEyMjcvMTcvMDQvMC8wMWNhOTE1NTU4OGM5MWI2MzYwOTMyN2I3ZTJmMDFlZC5qcGciLCJiaW8iOiLmnKzmnaXml6DkuIDnianvvIzkuIDliIfnmobpmo_nvJheXyIsImlzX21hc3RlciI6dHJ1ZSwiaXNfaG9zdCI6dHJ1ZSwibWFzdGVyX25hbWUiOiLms5XluIgxMDAifSwibG9naW5fdHlwZSI6IiIsImF1ZCI6IkFueSIsImV4cCI6MTU4NTg4ODA0OCwianRpIjoiNGQ5NzczYmYtNmNmYS00Yjg4LWJkYWEtNWNlODA2ZDFlMzZhIiwiaWF0IjoxNTg1MTMyMDQ4LCJpc3MiOiJTWE9TIiwibmJmIjoxNTg1MTMyMDQ4fQ._YKX3a5wy_fCINcDWC4UDzCf5mYUtNCxNc4uWF-31W0'
        self.headers_get = {"authorization": "Bearer " + self.token}


    def Master_list(self):
        # 获取礼物列表接口
        url = self.host + conf.get("Master", "Gift_list")
        print(url)
        try:
            # log.warning("login_Type：%s" % self.login_type_text)
            # 对礼物列表接口发送请求
            ret = requests.get(url, headers=self.headers_get)
            print(ret.text)
            # 把返回结果转换成json格式
            ret_json=ret.json()
            log.info('`````code{}'.format(ret_json))

            if ret_json["code"] == 0:
                self.cookies = ret.cookies
                self.userId = ret.json()["data"]
                log.info("success")
                log.info(ret)
                return ret_json
            else:
                log.warning("warning，response：%s" % ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    def grant_authorization(self,phone,code):
        """法师登录验证码授权"""
        url = self.host + conf.get("Master", "grant_authorization")
        print(url)
        # 接口参数
        data = json.dumps({ "phone": phone,"verifiable_code": code})
        print('data:'+data)
        try:
            # 对接口发送请求
            ret = requests.post(url=url, headers=self.headers_get,data=data)
            # print('ret:'+ret.text)
            # 把返回结果转换成json格式
            ret_json = ret.json()
            if ret_json["code"] == 0:
                self.cookies = ret.cookies
                self.login_random=ret.json()["data"]["login_random"]
                print("login_random:" + self.login_random)
                log.info("success")
                log.info(ret)
                return ret_json
            else:
                log.warning("warning，response：%s" % ret_json)
                return False
        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    def login_Master(self,phone):
        """法师登录接口"""
        url=self.host+conf.get('Master','login_Master')
        # 获取login_random
        login_random=self.login_random
        print("login_random:" + self.login_random)
        # 接口参数
        data = json.dumps({"phone": phone, "login_random": login_random})
        try:
            # 对接口发送请求
            ret = requests.post(url=url, headers=self.headers_get,data=data)
            # print('ret:'+ret.text)
            # 把返回结果转换成json格式
            ret_json = ret.json()
            if ret_json["code"] == 0:
                self.cookies = ret.cookies
                self.userId = ret.json()["data"]
                log.info("success")
                log.info(ret)
                return ret_json
            else:
                log.warning("warning，response：%s" % ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False










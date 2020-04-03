import unittest
import requests
import json

class case1(unittest.TestCase):
    def setUp(self):
        # 法师列表的url

        url = "https://temple.dev.renrenfo.cn:2443/ts/v2/temple/app/v4/temple/61/masters/338"
        token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWYiOjE1ODc1NTEyNDgsIlRlbXBsZVVzZXIiOnsiaWQiOjI1OCwidXNlcl9pZCI6NTMzLCJ0ZW1wbGVfaWQiOjYxLCJjcmVhdGVkX2F0IjoiMjAxOS0xMS0yNiAxMToxNToyOCIsInVwZGF0ZWRfYXQiOiIyMDE5LTEyLTI3IDE3OjA0OjM3IiwidXBkYXRlX3VzZXJfbmFtZSI6MSwidXBkYXRlX2F2YXRhciI6MSwibmlja19uYW1lIjoi6YeK5byA5ouJIiwicGFzc3dvcmQiOiIkMnkkMTAkQTJjRjEvdXp3MVAwUG9VblpzaEtZdWJUbmRBVWZqUDZERy55c1RUbnhkR1dxazkwYTlvYzYiLCJhdmF0YXIiOiIvZ3JvdXAxL2RlZmF1bHQvMjAxOTEyMjcvMTcvMDQvMC8wMWNhOTE1NTU4OGM5MWI2MzYwOTMyN2I3ZTJmMDFlZC5qcGciLCJiaW8iOiLmnKzmnaXml6DkuIDnianvvIzkuIDliIfnmobpmo_nvJheXyIsImlzX21hc3RlciI6dHJ1ZSwiaXNfaG9zdCI6dHJ1ZSwibWFzdGVyX25hbWUiOiLms5XluIgxMDAifSwibG9naW5fdHlwZSI6IiIsImF1ZCI6IkFueSIsImV4cCI6MTU4NTg4ODA0OCwianRpIjoiNGQ5NzczYmYtNmNmYS00Yjg4LWJkYWEtNWNlODA2ZDFlMzZhIiwiaWF0IjoxNTg1MTMyMDQ4LCJpc3MiOiJTWE9TIiwibmJmIjoxNTg1MTMyMDQ4fQ._YKX3a5wy_fCINcDWC4UDzCf5mYUtNCxNc4uWF-31W0'
        headers = {"authorization": "Bearer "+token}
        # 发送get请求
        ret = requests.get(url,headers=headers)
        print(ret.text)
        print(json.loads(ret.text))



    def tearDown(self):
        print('执行结束')


    def test1(self):
        """法师列表"""
        pass


if __name__ == '__main__':
    unittest.main()

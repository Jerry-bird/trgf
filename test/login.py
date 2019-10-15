# class SSO(object):
import json
import unittest

import jsonpath as jsonpath


def get_token():
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
               "Origin": "https://test-admin2.hntrgf.com.cn"}
    url = 'https://test-admin2-api.hntrgf.com.cn/auth/login'
    data = {"username": "trgf", "password": "96e79218965eb72c92a549dd5a330112", "channel": "4"}
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    if response.status_code == 200:
        response = response.json()
        token = jsonpath.jsonpath(response, '$.data.Authorization')
        if token:
            return token[-1]
    return "Null"


import requests
#
#
# class Login(object):
#     def __init__(self, url, username, password):
#         self.url = url
#         self.username = username
#         self.password = password
#
#     def get_token(self):
#         data = {"username": self.username, "password": self.password, "channel": "4"}
#         response = requests.post(url=self.url, json=data)
#         print(response.json())
#         # if response.status_code == 200:
#         #     token = jsonpath.jsonpath(response.json(), '$.data.Authorization')
#         #     if token:
#         #         # return token[0]
#         #         print(token+'wewe')
#         #     else:
#         #         # return "null"
#         #         print('shibai')
#         # # return "未登录成功"
#         # print('shibail')
#
#
# if __name__ == '__main__':
#     sso = Login(url="https://test-admin2-api.hntrgf.com.cn/auth/login", username="trgf",
#                 password="96e79218965eb72c92a549dd5a330112")
#     t = sso.get_token
#     print(t)

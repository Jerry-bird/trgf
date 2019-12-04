# coding = utf-8

import jsonpath
import requests

from Conf.url import url_login_admin

url = url_login_admin


def auth_login_admin():
    # data1 = {"username": "trgf", "password": "96e79218965eb72c92a549dd5a330112", "channel": "4"}
    # res = requests.post(url, data=data1)
    # print(url)
    # # print(res.json())
    # # token_admin = jsonpath.jsonpath(res.json(), '$..Authorization')[0]
    # # print(token_admin)
    # # return token_admin

    res = requests.get(url)
    cookie_value = ''
    for key, value in res.cookies.items():
        cookie_value += key + '=' + value
    Cookie = cookie_value
    return Cookie


auth_login_admin()

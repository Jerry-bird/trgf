# coding = utf-8
import json
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig

url = ReadConfig().get_http('baseurl_admin2') + '/auth/login'


def auth_login():
    data1 = {"username": "trgf", "password": "96e79218965eb72c92a549dd5a330112", "channel": "4"}
    res = requests.post(url, json=data1)
    # print(res.json())
    token = jsonpath.jsonpath(res.json(), '$..Authorization')[0]
    return token




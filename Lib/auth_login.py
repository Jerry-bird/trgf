# coding = utf-8

import jsonpath
import requests

from Conf.url import url_login_admin2
from MainExecute.readConfig import ReadConfig

url = url_login_admin2


def auth_login():
    data1 = {"username": "trgf", "password": "69dda505b57a84a3b85557d463bfc683", "channel": "4"}
    res = requests.post(url, json=data1)
    # print(res.json())
    token = jsonpath.jsonpath(res.json(), '$..Authorization')[0]
    return token




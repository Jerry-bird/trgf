import jsonpath
import requests

from Conf.url import url_config_cash
from Lib.headers import heads


# 获取提现方式
def config_cash():
    url = url_config_cash
    res = requests.get(url=url, params=None, headers=heads)
    # print(res.json())
    cashTerminal = jsonpath.jsonpath(res.json(), '$..cashTerminal')[0]
    # print(cashTerminal, type(cashTerminal))
    return cashTerminal


config_cash()

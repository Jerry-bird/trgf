import unittest

import jsonpath
import requests

from Conf.url import url_account_info
from Lib.headers import heads


# 获取账号配置信息--使用银行可提现的金额限制

def test_account_info():
    url = url_account_info
    res = requests.get(url=url, params=None, headers=heads)
    bankWithdrawLower = jsonpath.jsonpath(res.json(), '$..bankWithdrawLower')[0]
    # print(type(bankWithdrawLower))
    return bankWithdrawLower


test_account_info()

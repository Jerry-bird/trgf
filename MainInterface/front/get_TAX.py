import jsonpath
import requests

from Conf.url import url_get_TAX
from Lib.headers import heads


# 获取税率

def get_TAX():
    url = url_get_TAX
    res = requests.get(url=url, params=None, headers=heads)
    # print(res.json())
    tax_rate = jsonpath.jsonpath(res.json(), '$..captionchn')[0]
    # print(tax_rate)
    return tax_rate


get_TAX()

import jsonpath
import requests

from Conf.url import url_bank_meta
from Lib.headers import heads


class BankMeta(object):
    def test_bank_meta(self):
        cardNo = input("请输入你的银行卡号：")
        # print(cardNo)
        # cardNo = '6214837210715417'
        url = url_bank_meta + cardNo
        # print(url)
        res = requests.get(url=url, params=None, headers=heads)
        # print(res.json())
        bankName = jsonpath.jsonpath(res.json(), '$..bankName')[0]
        bankCode = jsonpath.jsonpath(res.json(), '$..bankCode')[0]
        cardNo = jsonpath.jsonpath(res.json(), '$..cardNo')[0]
        return bankName, bankCode, cardNo


if __name__ == '__main__':
    t = BankMeta()
    t.test_bank_meta()

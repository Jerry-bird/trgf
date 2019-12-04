import jsonpath
import requests

from Conf.url import url_use_bank
from Lib.headers import heads
from MainInterface.front.bank_sign import bank_sign


class UseBank(object):
    def test_use_bank(self):
        url = url_use_bank
        res = requests.get(url=url, params=None, headers=heads)
        # print(res.json())
        if 'memberBankCard' in res.text:
            payChannel = jsonpath.jsonpath(res.json(), '$..payChannel')[0]
            bankName = jsonpath.jsonpath(res.json(), '$...bankName')[0]
            bankCode = jsonpath.jsonpath(res.json(), '$...bankCode')[0]
            realName = jsonpath.jsonpath(res.json(), '$...realName')[0]
            mobile = jsonpath.jsonpath(res.json(), '$...mobile')[0]
            cardNo = jsonpath.jsonpath(res.json(), '$...cardNo')[0]
            return payChannel, bankName, bankCode, realName, mobile,cardNo
        else:
            bank_sign()
            self.test_use_bank()


if __name__ == '__main__':
    t = UseBank()
    t.test_use_bank()

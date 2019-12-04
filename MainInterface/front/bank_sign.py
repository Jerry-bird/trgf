import json

import requests

from Conf.url import url_bank_sign
from Lib.headers import heads
from MainInterface.front.bank_meta import BankMeta
from MainInterface.front.get_info import GetInfo


def bank_sign():
    url = url_bank_sign
    bank_name = BankMeta().test_bank_meta()[0]
    bankCode = BankMeta().test_bank_meta()[1]
    cardNo = BankMeta().test_bank_meta()[2]
    conNo = GetInfo().test_get_info()[2]
    conName = GetInfo().test_get_info()[7]
    # print(bank_name, bankCode, cardNo)
    data = {"mobile": "13974966933", "bankName": bank_name, "cardNo": cardNo, "bankCode": bankCode,
            "realName": "李鹏", "templateId": "341", "conNo": conNo, "identity": "41022519890521155x",
            "conName": conName}
    # print(data)
    res = requests.post(url=url, data=json.dumps(data), headers=heads)
    # print(res.json())


if __name__ == '__main__':
    bank_sign()

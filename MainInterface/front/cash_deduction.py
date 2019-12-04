import random
import unittest

import jsonpath
import requests

from Conf.url import url_cash_deduction
from Lib.headers import heads
from MainInterface.front.commission_app import CommissionApp
from MainInterface.front.get_TAX import get_TAX


class CashDeduction(unittest.TestCase):
    def test_cash_deduction(self):
        # 获取 随机得提现金额
        maxAllowCount = CommissionApp().test_commission_app()[0]
        # print(maxAllowCount)
        amount_put = round(random.uniform(0, maxAllowCount), 2)
        # amount_put = 0.5
        # print(amount_put)
        url = url_cash_deduction + str(amount_put)
        res = requests.put(url=url, params=None, headers=heads)
        # print(res.json())
        # 该接口返回的税率
        tax = float('%.2f' % float(jsonpath.jsonpath(res.json(), '$..tax')[0]))
        # 返回的税额
        taxAmount = jsonpath.jsonpath(res.json(), '$..taxAmount')[0]
        # 实际到账金额
        actualAmount = jsonpath.jsonpath(res.json(), '$..actualAmount')
        # 税率接口返回税率
        tax_test = float(get_TAX())
        # 计算税额
        taxAmount_test = float('%.2f' % float(amount_put * tax_test / 100))
        # print(tax_test, type(taxAmount), type(taxAmount_test))
        # print(tax_test, taxAmount, taxAmount_test)
        self.assertEqual(taxAmount, taxAmount_test)
        return actualAmount, amount_put


if __name__ == '__main__':
    t = CashDeduction()
    t.test_cash_deduction()

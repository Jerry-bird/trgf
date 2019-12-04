# coding = utf-8
import json
import unittest

import jsonpath
import requests

from Conf.url import url_pay_to_pay
from Lib.headers import heads
from MainInterface.front.order_put import OrderPut


class PayToPay(unittest.TestCase):
    def test_pay_to_pay(self):
        url = url_pay_to_pay
        orderId = OrderPut().test_order_put()[0]
        data = {"orderId": orderId, "tradeType": "APP"}
        res = requests.post(url, data=json.dumps(data), headers=heads)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = PayToPay()
    t.test_pay_to_pay()

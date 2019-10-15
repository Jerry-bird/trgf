# coding = utf-8
import json
import unittest

import jsonpath
import requests

from Lib.headers import heads1
from MainInterface.order_put import OrderPut

url = 'https://test-admin2-api.hntrgf.com.cn/biz/orders/savepay'


class OrdersSavepay(unittest.TestCase):
    def test_orders_savepay(self):
        orderId = OrderPut().test_order_put()[0]
        data1 = {"operateRemark": "测试", "orderId": orderId}
        # print(data1)
        res = requests.put(url, data=json.dumps(data1), headers=heads1)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = OrdersSavepay()
    t.test_orders_savepay()

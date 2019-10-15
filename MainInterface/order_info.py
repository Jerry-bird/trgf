# coding = utf-8
import unittest

import jsonpath
import requests

from Lib.headers import heads
from MainExecute.readConfig import ReadConfig
from MainInterface.get_info import GetInfo
from MainInterface.index_all_list import GetList
from MainInterface.order_put import OrderPut

orderId = OrderPut().test_order_put()[0]
url = ReadConfig().get_http('baseurl') + '/ms-order/order/info/' + orderId

print(url)


class OrderInfo(unittest.TestCase):
    def test_order_info(self):
        res = requests.get(url, params=None, headers=heads)
        print(res.json())
        orderId_res = jsonpath.jsonpath(res.json(), '$..orderId')[0]
        conId_res = jsonpath.jsonpath(res.json(), '$..conId')[0]
        orderTotal_res = float('%.2f' % (jsonpath.jsonpath(res.json(), '$..orderTotal')[0]))
        productId_res = jsonpath.jsonpath(res.json(), '$...productId')[0]
        # print(productId_res)
        conId = GetInfo().test_get_info()
        # print(conId)
        orderTotal = OrderPut().test_order_put()[2]
        productId = GetList().test_index_list()[0]
        # print(orderTotal)
        self.assertEqual(productId_res, productId)
        self.assertEqual(orderTotal, orderTotal_res)
        self.assertEqual(conId_res, conId)
        self.assertEqual(orderId_res, orderId)


if __name__ == '__main__':
    t = OrderInfo()
    t.test_order_info()

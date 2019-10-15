# coding = utf-8
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-order/order/cherk/add'


class OrderCheckAdd(unittest.TestCase):
    def test_order_check_add(self):
        res = requests.get(url, params=None, headers=heads)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = OrderCheckAdd()
    t.test_order_check_add()

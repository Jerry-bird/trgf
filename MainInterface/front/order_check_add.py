# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.url import url_check_add
from Lib.headers import heads


class OrderCheckAdd(unittest.TestCase):
    def test_order_check_add(self):
        url = url_check_add
        res = requests.get(url, params=None, headers=heads)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = OrderCheckAdd()
    t.test_order_check_add()

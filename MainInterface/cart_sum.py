# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-goods/cart/sum'


class CartSum(unittest.TestCase):
    def test_cart_sum(self):
        res = requests.get(url, params=None, headers=heads)
        count = jsonpath.jsonpath(res.json(), '$.data')[0]
        # print(count)
        oraDb = Oracle()
        sql = '''Select Count(1) From bas_cust_cart t Where t.con_id =:con_id'''
        con_id = 'e08296fa2ed84476890c8eb7d4d2b78f'
        lists = oraDb.queryBy(sql, {'con_id': con_id})[0][0]
        # print(lists)
        self.assertEqual(count, lists)


if __name__ == '__main__':
    t = CartSum()
    t.test_cart_sum()

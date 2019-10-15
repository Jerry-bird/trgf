# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-goods/cart/list'


class CartList(unittest.TestCase):
    def test_cart_list(self):
        res = requests.get(url, params=None, headers=heads)
        product_sum = jsonpath.jsonpath(res.json(), '$...productId')[0]
        oraDb = Oracle()
        sql = '''Select t.product_id From bas_cust_cart t Where t.con_id =:con_id'''
        con_id = 'e08296fa2ed84476890c8eb7d4d2b78f'
        lists = oraDb.queryBy(sql, {'con_id': con_id})[0][0]
        self.assertEqual(product_sum, lists, msg='数据错误')


if __name__ == '__main__':
    t = CartList()
    t.test_cart_list()

# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_cart_list
from Lib.headers import heads


class CartList(unittest.TestCase):
    """我是一个购物车列表的接口"""

    def test_cart_list(self):
        url = url_cart_list
        res = requests.get(url, params=None, headers=heads)
        # print(res.json())
        product_sum = jsonpath.jsonpath(res.json(), '$...productId')
        # print(product_sum)
        oraDb = Oracle()
        sql = '''Select t.product_id From bas_cust_cart t Where t.con_id =:con_id'''
        con_id = 'e08296fa2ed84476890c8eb7d4d2b78f'
        # lists = oraDb.queryBy(sql, {'con_id': con_id})[0][0]
        # self.assertEqual(product_sum, lists, msg='数据错误')
        product_sum_cart = jsonpath.jsonpath(res.json(), '$..data')
        return product_sum_cart


if __name__ == '__main__':
    t = CartList()
    t.test_cart_list()

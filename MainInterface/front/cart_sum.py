# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_cart_sum
from Lib.headers import heads
from MainInterface.front.get_info import GetInfo

'''因IOS修复问题修改，IOS请求cart_sum接口不会返回商品数量'''


class CartSum(unittest.TestCase):
    def test_cart_sum(self):
        url = url_cart_sum
        res = requests.get(url, params=None, headers=heads)
        print(url, heads, res.json())
        count = jsonpath.jsonpath(res.json(), '$.data')
        print(count)
        # print(count)
        oraDb = Oracle()
        con_id = GetInfo().test_get_info()[0]
        print(con_id)
        sql = '''Select Sum(product_num) From bas_cust_cart t Where t.con_id =:con_id'''
        lists = oraDb.queryBy(sql, {'con_id': con_id})[0][0]
        print(lists)
        # self.assertEqual(count, lists)


if __name__ == '__main__':
    t = CartSum()
    t.test_cart_sum()

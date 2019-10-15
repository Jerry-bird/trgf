# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from MainExecute.readConfig import ReadConfig
from Lib.headers import heads
from MainInterface.index_all_list import GetList

url = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/confirm/query/quick'


class ConfirmQuery(unittest.TestCase):
    def test_confirm_query_quick(self):
        product_id = GetList().test_index_list()[0]
        data1 = {"productId": product_id}
        res = requests.post(url, json=data1, headers=heads)
        firstPrice = jsonpath.jsonpath(res.json(), '$...firstPrice')[0]
        rePrice = jsonpath.jsonpath(res.json(), '$...rePrice')[0]
        productPrice = jsonpath.jsonpath(res.json(), '$...productPrice')[0]
        return firstPrice, rePrice, productPrice
        oraDb = Oracle()
        sql = '''Select (1-t.befor_agent/100)*t.buy_price,(1-t.after_agent/100)*t.buy_price From 
        pnt_product  t Where t.product_id =:product_id'''
        lists = oraDb.queryBy(sql, {'product_id': product_id})
        self.assertEqual(firstPrice, lists[0][0])
        self.assertEqual(rePrice, lists[0][1])


if __name__ == '__main__':
    t = ConfirmQuery()
    t.test_confirm_query_quick()

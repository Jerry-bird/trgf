import json
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_cart_insert
from Lib.headers import heads
from MainInterface.front.get_index_sku import IndexSku


class CartInsert(unittest.TestCase):

    # 添加新客专享商品进入购物车，由于下单原因，暂时去除
    # def test_cart_insert_new(self):
    #     url = url_cart_insert
    #     oraDb = Oracle()
    #     product_name = 'test_new'
    #     sql = '''Select product_id From pnt_product  Where product_name =:product_name'''
    #     product_id_new = oraDb.queryBy(sql, {'product_name': product_name})[0][0]
    #     data = {"productId": product_id_new, "productNum": 1, "skuId": ""}
    #     res = requests.post(url=url, data=json.dumps(data), headers=heads)
    #     msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
    #     self.assertEqual(msg, '成功')

    # 添加无sku商品进入购物车
    def test_cart_insert_wusku(self):
        url = url_cart_insert
        oraDb = Oracle()
        product_name = 'test_wusku'
        sql = '''Select product_id From pnt_product  Where product_name =:product_name'''
        product_id_new = oraDb.queryBy(sql, {'product_name': product_name})[0][0]
        data = {"productId": product_id_new, "productNum": 1, "skuId": ""}
        res = requests.post(url=url, data=json.dumps(data), headers=heads)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')

    # 添加sku商品进入购物车
    def test_cart_insert_sku(self):
        url = url_cart_insert
        oraDb = Oracle()
        product_name = 'test_sku'
        sql = '''Select product_id From pnt_product  Where product_name =:product_name'''
        product_id_new = oraDb.queryBy(sql, {'product_name': product_name})[0][0]
        sku_id = IndexSku().test_get_index()
        for i in sku_id:
            data = {"productId": product_id_new, "productNum": 1, "skuId": i}
            res = requests.post(url=url, data=json.dumps(data), headers=heads)
            msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
            self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = CartInsert()
    t.test_cart_insert_new()
    t.test_cart_insert_wusku()

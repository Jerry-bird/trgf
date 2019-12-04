# coding=utf-8
import unittest

import jsonpath
import requests

from Conf.url import url_index_list
from Lib.headers import heads


# 首页商品列表
class GetList(unittest.TestCase):
    def test_index_list(self):
        url = url_index_list
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        msg2 = jsonpath.jsonpath(res.json(), '$...productId')
        # print(msg2)
        self.assertEqual(msg1, '成功')
        return msg2


#        oraDb = Oracle()
#        sql = """Select t.product_id From pnt_product t, pnt_brand d
# Where t.product_type In ('0','1') And t.pro_status In ('0','4') And  t.shop_type Like '%app%' And t.brand_id = d.id
# Order By d.c_index Desc ,t.display_sequence Desc"""
#        lists = oraDb.queryBy(sql)
#        msg3 = []
#        for i in lists:
#            msg3.append(i[0])
#        print(msg3)
#        self.assertEqual(msg2, msg3)


if __name__ == '__main__':
    t = GetList()
    t.test_index_list()

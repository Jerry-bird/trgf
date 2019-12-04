# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_product_review
from Lib.headers import heads
from MainInterface.front.index_all_list import GetList


class CountProductReview(unittest.TestCase):
    def test_count_product_review(self):
        product_id = GetList().test_index_list()[0]
        url = url_product_review + product_id
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')
        oraDb = Oracle()
        sql = '''Select Count(1) From pnt_product_reviews  t Where t.product_id =: product_id'''
        lists = oraDb.queryBy(sql, {'product_id': 'product_id'})[0][0]
        msg2 = jsonpath.jsonpath(res.json(), '$..count')[0]
        self.assertEqual(msg2, lists)


if __name__ == '__main__':
    t = CountProductReview()
    t.test_count_product_review()

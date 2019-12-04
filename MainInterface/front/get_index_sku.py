import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_index_sku
from Lib.headers import heads


class IndexSku(unittest.TestCase):
    def test_get_index(self):
        oraDb = Oracle()
        product_name = 'test_sku'
        sql = '''Select product_id From pnt_product  Where product_name =:product_name'''
        product_id_sku = oraDb.queryBy(sql, {'product_name': product_name})[0][0]
        url = url_index_sku + product_id_sku
        res = requests.get(url=url, params=None, headers=heads)
        code = jsonpath.jsonpath(res.json(), '$.code')[0]
        if code == '0':
            sku_id = jsonpath.jsonpath(res.json(), '$..id')
            return sku_id
        else:
            print('接口报错')


if __name__ == '__main__':
    t = IndexSku()
    t.test_get_index()

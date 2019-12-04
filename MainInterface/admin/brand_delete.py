import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_brand_delete
from Lib.headers import heads1


class BrandSave(unittest.TestCase):
    def test_brand_save(self, mgs=None):
        oraDb = Oracle()
        brand_no = 'test'
        sql = '''Select t.id From pnt_brand t Where t.brand_no = :brand_no'''
        lists = oraDb.queryBy(sql, {'brand_no': brand_no})
        brand_id = lists[0][0]
        url = url_brand_delete + brand_id
        res = requests.delete(url=url, params=None, headers=heads1)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = BrandSave()
    t.test_brand_save()

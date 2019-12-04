# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.url import url_index_detail
from Lib.headers import heads
from MainInterface.front.index_all_list import GetList

product_id = GetList().test_index_list()[0]


class IndexDetailNew(unittest.TestCase):
    def test_index_detail_new(self):
        url = url_index_detail + product_id
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = IndexDetailNew()
    t.test_index_detail_new()

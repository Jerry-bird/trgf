# coding = utf-8
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads
from MainInterface.index_all_list import GetList

product_id = GetList().test_index_list()[0]
# print(product_id)
url = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/detail/new/' + product_id


class IndexDetailNew(unittest.TestCase):
    def test_index_detail_new(self):
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = IndexDetailNew()
    t.test_index_detail_new()

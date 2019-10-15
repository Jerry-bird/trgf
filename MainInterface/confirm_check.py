# coding = utf-8
import json
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads
from MainInterface.index_all_list import GetList

url = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/confirm/check'


class ConfirmCheck(unittest.TestCase):
    def test_confirm_check(self):
        product_id = GetList().test_index_list()[0]
        data1 = {"freightProductParamList": [{"num": 1, "productId": product_id}]}
        data2 = json.dumps(data1)
        res = requests.post(url, data=data2, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = ConfirmCheck()
    t.test_confirm_check()

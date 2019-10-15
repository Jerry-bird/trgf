# coding = utf-8
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-promotion/promotion/advertisement/list?adPosition=1'


class AdvertisementList(unittest.TestCase):
    def test_advertisement_list(self):
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = AdvertisementList()
    t.test_advertisement_list()
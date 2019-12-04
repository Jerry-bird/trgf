import json
import unittest

import jsonpath
import requests

from Conf.url import url_brand_save
from Lib.headers import heads1


# 品牌的新增

class BrandSave(unittest.TestCase):
    def test_brand_save(self):
        url = url_brand_save
        data = {"brandNo": "test", "brandName": "自动化品牌", "cindex": "99999"}
        res = requests.post(url, data=json.dumps(data), headers=heads1)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = BrandSave()
    t.test_brand_save()

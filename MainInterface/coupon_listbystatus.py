#  coding = utf-8
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-promotion/coupon/listbystatus'


class CouponListByStatus(unittest.TestCase):
    def test_coupon_list_by_status(self):
        res = requests.get(url, params=None, headers=heads)

        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]

        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = CouponListByStatus()
    t.test_coupon_list_by_status()

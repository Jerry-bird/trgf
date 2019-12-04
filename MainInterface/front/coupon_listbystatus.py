#  coding = utf-8
import unittest

import jsonpath
import requests

from Conf.url import url_coupon_list
from Lib.headers import heads



class CouponListByStatus(unittest.TestCase):
    def test_coupon_list_by_status(self):
        url = url_coupon_list
        res = requests.get(url, params=None, headers=heads)

        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]

        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = CouponListByStatus()
    t.test_coupon_list_by_status()

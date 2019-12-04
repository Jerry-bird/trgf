# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.url import url_coupon_home_list
from Lib.headers import heads


class CouponHomepageList(unittest.TestCase):
    def test_coupon_homepage_list(self):
        url = url_coupon_home_list
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if  __name__ == '__main__':
    t = CouponHomepageList
    t.test_coupon_homepage_list()
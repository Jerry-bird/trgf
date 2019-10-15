# coding = utf-8
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-promotion/coupon-detail/active/payed/coupon'


class ActivePayedCoupon(unittest.TestCase):
    def test_active_payed_coupon(self):
        res = requests.post(url, json=None, headers=heads)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = ActivePayedCoupon()
    t.test_active_payed_coupon()

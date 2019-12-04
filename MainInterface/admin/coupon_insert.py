import json
import unittest

import jsonpath
import requests

from Conf.mySql import Mysql
from Conf.url import url_coupon_insert, url_resource_user
from Lib.headers import heads1


class CouponInsert(unittest.TestCase):
    def test_coupon_insert(self):
        url = url_coupon_insert
        data = {"memberType": "3", "couponType": "0", "scopeType": "0", "conditionType": "0", "releaseType": "0",
                "memberLimit": "1", "conditionValue": "10", "releaseValue": "", "businessAssumePercent": "1",
                "couponName": "test_lp", "couponValue": "5", "releaseTotal": "100000", "yxqType": "1",
                "validityExpiresTime": "100", "platformAssumePercent": "1", "conditionDesc": "1", "couponDesc": "1",
                "lapseNotifySecondVo": "10", "lapseMsgTemplateNo": "COUPON_002", "couponClient": "app,wechat,xcx,h5",
                "scopeProduct": ""}
        res = requests.post(url=url, data=json.dumps(data), headers=heads1)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')

    def test_coupon_update(self):
        oraDb = Mysql()
        coupon_name = 'test_lp'
        sql = '''SELECT * FROM sp_coupon  WHERE enabled= 1 and coupon_name =(%s)'''
        coupon_id = oraDb.queryBy(sql, coupon_name)[0][0]
        print(coupon_id)
        url = url_resource_user + str(coupon_id)
        print(url)
        data = {"cause": "测试", "status": "1"}
        res = requests.put(url=url, data=json.dumps(data), headers=heads1)
        print(res.json())
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = CouponInsert()
    t.test_coupon_insert()
    t.test_coupon_update()

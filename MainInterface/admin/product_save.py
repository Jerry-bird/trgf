import json
import unittest

import jsonpath
import requests

from Conf.url import url_product_save, url_product_shelve, url_share_update
from Lib.headers import heads1


class ProductSave_demo(object):
    def __init__(self):
        self.product_id = None

    # 新增商品--普通商品
    def product_save(self):
        url = url_product_save
        data = {"proStatus": "2", "validDate": "2099-01-01", "beforAgent": "0", "afterAgent": "20", "beforAgent1": "10",
                "afterAgent1": "2", "groupPercent": "0", "corePercent": "100", "depentCommision": "0",
                "useSizeHelper": "0", "useStatus": "1", "rewardStatus": "0", "servicePercent": "12",
                "costPercent": "60", "beforePromotionPercent": "29", "afterPromotionPercent": "9", "isGroup": "2",
                "productName": "test_wusku", "abbName": "test_wusku", "spec": "test", "productCode": "test_wusku",
                "brandId": "926EC4765CC24FC0ACE924E4B07D4E46", "pweightUnit": "kg", "tmplId": "30", "hasSku": "0",
                "productType": "0", "retailPrice": "99", "initNumber": "10000",
                "categoryAll": "64008D09F9DF48BABB96BFBB3715720A,FAE3EE1CE69A4E2F87ABFB5F35D2B576,"
                               "52DE88DBC67040389109E30C00F6D267",
                "category": "52DE88DBC67040389109E30C00F6D267"}
        res = requests.post(url=url, data=json.dumps(data), headers=heads1)
        self.product_id = jsonpath.jsonpath(res.json(), '$.data')[0]
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        if msg == '成功':
            return self.product_id
        else:
            False

    # 新增商品的显示终端
    def share_doc(self):
        url = url_share_update + self.product_id
        data = {"displaySequence": "1", "briefDescription": "测试", "shopType": "app,h5,wechat,xcx"}
        res = requests.post(url=url, data=json.dumps(data), headers=heads1)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        if msg == '成功':
            return self.product_id
        else:
            False

    #  商品的上架
    def product_shelve(self):
        url = url_product_shelve + self.product_id
        res = requests.put(url, params=None, headers=heads1)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        if msg == '成功':
            return self.product_id
        else:
            False


class ProductSave(unittest.TestCase):
    def test_product_add(self):
        t = ProductSave_demo()
        t.product_save()
        t.share_doc()
        t.product_shelve



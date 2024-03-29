# coding = utf-8
import json
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from MainInterface.address_isdefault import AddressIsdefault
from MainInterface.confirm_query_quick import ConfirmQuery
from MainInterface.get_freight import GetFreight
from Lib.headers import heads
from MainInterface.index_all_list import GetList

url = ReadConfig().get_http('baseurl') + '/ms-order/order-put/order/put/freight'


class OrderPutFreight(unittest.TestCase):
    def test_order_put_freight(self):
        # 获取地址信息
        memberAddressId = AddressIsdefault().test_address_isdefault()[0]
        # 获取商品id
        product_id = GetList().test_index_list()[0]
        # 获取商品首购价
        firstPrice = ConfirmQuery().test_confirm_query_quick()[0]
        # 获取商品复购价
        rePrice = ConfirmQuery().test_confirm_query_quick()[1]
        # 获取商品价格
        productPrice = ConfirmQuery().test_confirm_query_quick()[2]
        # 入参格式化
        data = json.dumps({"isUsePoints": "1", "memberAddressId": memberAddressId, "putProductItemsList": [
            {"productPrice": productPrice, "productNum": 1, "productId": product_id,
             "firstPrice": firstPrice, "rePrice": rePrice}]})
        # 获取返回
        res = requests.post(url, data=data, headers=heads)
        # 获取普通快递运费
        freight = float('%.2f' % (jsonpath.jsonpath(res.json(), '$..adjustedFreight')[0]))
        # 获取京东快递运费
        freightJd = float('%.2f' % (jsonpath.jsonpath(res.json(), '$..adjustedFreightJd')[0]))
        # print(freightJd)
        # 获取mysql普通快递运费
        freight_mysql = float('%.2f' % (GetFreight().get_freight()[0]))
        # 获取mysql京东快递运费
        freightJd_mysql = float('%.2f' % (GetFreight().get_freight()[1]))
        # 断言普通快递运费是否正确
        self.assertEqual(freight, freight_mysql)
        # 断言京东快递运费是否正确
        self.assertEqual(freightJd, freightJd_mysql)
        return freight, freightJd


if __name__ == '__main__':
    t = OrderPutFreight()
    t.test_order_put_freight()

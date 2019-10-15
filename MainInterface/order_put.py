# coding = utf-8
import json
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from MainInterface.address_isdefault import AddressIsdefault
from Lib.headers import heads
from MainInterface.index_all_list import GetList
from MainInterface.order_put_freight import OrderPutFreight
from MainInterface.put_price import PutPrice

url = ReadConfig().get_http('baseurl') + '/ms-order/order-put/order/member/put'


class OrderPut(unittest.TestCase):
    def test_order_put(self):
        # 获取商品id
        product_id = GetList().test_index_list()[0]
        # 获取地址id
        memberAddressId = AddressIsdefault().test_address_isdefault()[0]
        data = {"remark": "", "isFreightFree": "0", "putType": 1, "paymentTypeid": "4",
                "itemsList": [{"quantity": 1, "productId": product_id}], "isJdexpress": 0,
                "memberAddressId": memberAddressId, "orderSource": "5", "isUsePoints": "1", "orderType": "1"}
        res = requests.post(url, data=json.dumps(data), headers=heads)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        orderTotal = jsonpath.jsonpath(res.json(), '$..orderTotal')[0]
        orderTotal_test = float(PutPrice().test_put_price()) + float(OrderPutFreight().test_order_put_freight()[0])
        # print(msg1, orderTotal, orderTotal_test)
        # print(product_id)
        # print(orderTotal)
        self.assertEqual(msg1, '成功')
        self.assertEqual(orderTotal, orderTotal_test)
        orderId = jsonpath.jsonpath(res.json(), '$..orderId')[0]
        orderNo = jsonpath.jsonpath(res.json(), '$..orderNo')[0]
        return orderId, orderNo, orderTotal


if __name__ == '__main__':
    t = OrderPut()
    t.test_order_put()

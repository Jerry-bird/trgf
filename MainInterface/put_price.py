# coding = utf-8
import json
import time
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from MainInterface.address_isdefault import AddressIsdefault
from MainInterface.confirm_query_quick import ConfirmQuery
from Lib.headers import heads
from MainInterface.index_all_list import GetList

url = ReadConfig().get_http('baseurl') + '/ms-order/order-put/order/put/price'


class PutPrice(unittest.TestCase):
    def test_put_price(self):
        # 获取商品首购价
        firstPrice = ConfirmQuery().test_confirm_query_quick()[0]
        # 获取商品复购价
        rePrice = ConfirmQuery().test_confirm_query_quick()[1]
        # 获取商品价格
        productPrice = ConfirmQuery().test_confirm_query_quick()[2]
        # 获取商品id
        product_id = GetList().test_index_list()[0]
        # 获取地址信息
        memberAddressId = AddressIsdefault().test_address_isdefault()[0]
        # 获取时间戳
        tag = time.time()
        # 暂时定义商品数量
        productNum = '1'
        data = {"putProductItemsList": [
            {"productPrice": productPrice, "productNum": productNum, "productId": product_id,
             "firstPrice": firstPrice, "rePrice": rePrice}], "memberAddressId": memberAddressId, "isUsePoints": "1",
            "tag": tag}
        res = requests.post(url, data=json.dumps(data), headers=heads)
        # print(res.json())
        # 商品总价
        productTotal = jsonpath.jsonpath(res.json(), '$..productTotal')[0]
        # 商品复购价总价
        productPriceSum = jsonpath.jsonpath(res.json(), '$..productPriceSum')[0]
        # 商品折扣的总价
        disProductPriceSum = jsonpath.jsonpath(res.json(), '$..disProdcutPriceSum')[0]
        # 优惠券抵扣的总价
        couponAmountSum = jsonpath.jsonpath(res.json(), '$..couponAmountSum')[0]
        # 需付款总价
        payableAmount = jsonpath.jsonpath(res.json(), '$..payableAmout')[0]
        # 商品价格*数量
        productTotal_test = float('%.2f' % productPrice) * int(productNum)
        # 商品复购价*数量
        productPriceSum_test = float('%.2f' % rePrice) * int(productNum)
        # print(productPriceSum_test)
        # 　商品抵扣金额
        disProductPriceSum_test = float('%.2f' % (productTotal_test - productPriceSum_test))
        # print(disProductPriceSum_test)
        # 此时未计算入积分抵扣和优惠券
        payableAmount_test = productPriceSum_test
        # 断言商品总价是否正确
        self.assertEqual(productTotal, productTotal_test)
        # 断言商品实购总价是否正确
        # print(productPriceSum,productPriceSum_test)
        self.assertEqual(productPriceSum, productPriceSum_test)
        # 商品的折扣总价是否正确
        self.assertEqual(disProductPriceSum, disProductPriceSum_test)
        # 断言应付金额总价是否正确
        self.assertEqual(payableAmount, payableAmount_test)
        # print(productPriceSum)
        return productPriceSum


if __name__ == '__main__':
    t = PutPrice()
    t.test_put_price()

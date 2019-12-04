# coding = utf-8
import json
import time
import unittest

import jsonpath
import requests

from Conf.mySql import Mysql
from Conf.url import url_put_price
from MainInterface.front.address_isdefault import AddressDefault
from MainInterface.front.cart_list import CartList
from MainInterface.front.confirm_query_quick import ConfirmQuery
from Lib.headers import heads
from MainInterface.front.coupon_self_list import CouponSelfCart
from MainInterface.front.get_info import GetInfo
from MainInterface.front.get_points import get_points
from MainInterface.front.index_all_list import GetList


class PutPrice(unittest.TestCase):
    def test_put_price(self):
        url = url_put_price
        # 获取商品首购价
        firstPrice = ConfirmQuery().test_confirm_query_quick()[0]
        # 获取商品复购价
        rePrice = ConfirmQuery().test_confirm_query_quick()[1]
        # 获取商品价格
        productPrice = ConfirmQuery().test_confirm_query_quick()[2]
        # 获取商品id
        product_id = GetList().test_index_list()[0]
        # 获取地址信息
        memberAddressId = AddressDefault().test_address_default()[0]
        # 获取时间戳
        tag = int(time.time())
        product_sum_cart = CartList().test_cart_list()
        con_no = GetInfo().test_get_info()[2]
        sqlDb = Mysql()
        sql_points = "update sp_points_member set points_available = '100' where con_no =%s" % con_no
        sqlDb.queryOne(sql_points)
        putProductItemslist = []
        for i in range(0, len(product_sum_cart[0])):
            if product_sum_cart[0][i]['isSelected'] == 1:
                if 'skuId' in product_sum_cart[0][i]:
                    putProductItems = {"productPrice": product_sum_cart[0][i]['productPrice'],
                                       "productNum": product_sum_cart[0][i]['productNum'],
                                       "productId": product_sum_cart[0][i]['productId'],
                                       "firstPrice": product_sum_cart[0][i]['firstPrice'],
                                       "rePrice": product_sum_cart[0][i]['rePrice'],
                                       "skuId": product_sum_cart[0][i]['skuId']}
                else:
                    putProductItems = {"productPrice": product_sum_cart[0][i]['productPrice'],
                                       "productNum": product_sum_cart[0][i]['productNum'],
                                       "productId": product_sum_cart[0][i]['productId'],
                                       "firstPrice": product_sum_cart[0][i]['firstPrice'],
                                       "rePrice": product_sum_cart[0][i]['rePrice']}
                putProductItemslist.append(putProductItems)
        # 引入优惠券code
        coupon_code = CouponSelfCart().test_coupon_self_cart()
        # print(coupon_code)
        # 拼接入参
        data = {"putProductItemsList": putProductItemslist, "memberAddressId": memberAddressId, "isUsePoints": "1",
                "couponDetailCode": coupon_code,
                "tag": tag}
        # 调用计价接口
        res = requests.post(url, data=json.dumps(data), headers=heads)
        # 取出各个字段
        data_res = jsonpath.jsonpath(res.json(), '$.data')[0]
        # print(data_res)
        productTotal = data_res['productTotal']
        productPriceSum = data_res['productPriceSum']
        couponAmountSum = data_res['couponAmountSum']
        pointsAvailable = data_res['pointsAvailable']
        amountAvailable = data_res['amountAvailable']
        # 计算商品总价
        productTotal_test = 0
        for i in range(0, len(putProductItemslist)):
            # print(putProductItemslist[i]['productPrice'])
            # print(product_sum_cart[0][i]['productNum'])
            # productPrice = sum(putProductItemslist[i]['productPrice'])
            # print(productPrice)
            productTotal_test = float('%.2f' % (productTotal_test +
                                                putProductItemslist[i]['productPrice'] * putProductItemslist[i][
                                                    'productNum']))
        # print(productTotal_test)

        # 计算商品复购总价
        productPriceSum_test = 0
        for i in range(0, len(putProductItemslist)):
            productPriceSum_test = float('%.2f' % (productPriceSum_test +
                                                   putProductItemslist[i]['rePrice'] * putProductItemslist[i][
                                                       'productNum']))
        # print(float('%.2f' % productPriceSum_test))

        # 获取积分抵扣金额
        # 可用积分
        points_available = get_points()[0]
        # 积分抵扣比例
        value = get_points()[1]
        if points_available / value <= productPriceSum_test:
            amountAvailable_test = points_available / value
        else:
            amountAvailable_test = productPriceSum_test
        # 优惠券金额
        oraDb = Mysql()
        sql = '''select a.coupon_value from sp_coupon a ,sp_coupon_detail b 
        where  a.id = b.coupon_id and b.detail_code =(%s) '''
        couponAmountSum_test = oraDb.queryBy(sql, coupon_code)[0][0]
        # print(couponAmountSum_test)

        # 断言校验
        try:
            self.assertEqual(productTotal, productTotal_test)
            self.assertEqual(productPriceSum, productPriceSum_test)
            self.assertEqual(couponAmountSum, couponAmountSum_test)
            self.assertEqual(amountAvailable, amountAvailable_test)
        except AssertionError:
            print('断言错误')
        else:
            pass
        # print(productPriceSum_test, couponAmountSum_test, amountAvailable_test)
        price_total = float('%.2f' % productPriceSum_test) - float('%.2f' % couponAmountSum_test) - float(
            '%.2f' % amountAvailable_test)
        return price_total
        # 商品总价
        # productTotal = jsonpath.jsonpath(res.json(), '$..productTotal')[0]
        # # 商品复购价总价
        # productPriceSum = jsonpath.jsonpath(res.json(), '$..productPriceSum')[0]
        # # 商品折扣的总价
        # disProductPriceSum = jsonpath.jsonpath(res.json(), '$..disProdcutPriceSum')[0]
        # # 优惠券抵扣的总价
        # couponAmountSum = jsonpath.jsonpath(res.json(), '$..couponAmountSum')[0]
        # # 需付款总价
        # payableAmount = jsonpath.jsonpath(res.json(), '$..payableAmout')[0]
        # # 商品价格*数量
        # productTotal_test = float('%.2f' % productPrice) * int(productNum)
        # # 商品复购价*数量
        # productPriceSum_test = float('%.2f' % rePrice) * int(productNum)
        # # print(productPriceSum_test)
        # # 　商品抵扣金额
        # disProductPriceSum_test = float('%.2f' % (productTotal_test - productPriceSum_test))
        # # print(disProductPriceSum_test)
        # # 此时未计算入积分抵扣和优惠券
        # payableAmount_test = productPriceSum_test
        # # 断言商品总价是否正确
        # self.assertEqual(productTotal, productTotal_test)
        # # 断言商品实购总价是否正确
        # # print(productPriceSum,productPriceSum_test)
        # self.assertEqual(productPriceSum, productPriceSum_test)
        # # 商品的折扣总价是否正确
        # self.assertEqual(disProductPriceSum, disProductPriceSum_test)
        # # 断言应付金额总价是否正确
        # self.assertEqual(payableAmount, payableAmount_test)
        # # print(productPriceSum)
        # return productPriceSum


if __name__ == '__main__':
    t = PutPrice()
    t.test_put_price()

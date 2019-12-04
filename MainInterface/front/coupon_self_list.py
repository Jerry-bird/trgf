import json
import unittest

import jsonpath
import requests

from Conf.url import url_coupon_self_list
from Lib.headers import heads
from MainInterface.front.cart_list import CartList
from MainInterface.front.get_info import GetInfo


class CouponSelfCart(unittest.TestCase):
    def test_coupon_self_cart(self):
        url = url_coupon_self_list
        contype = GetInfo().test_get_info()[1]
        product_sum_cart = CartList().test_cart_list()
        couponProductParamsList = []
        for i in range(0, len(product_sum_cart[0])):
            if product_sum_cart[0][i]['isSelected'] == 1:
                couponProductParams = {"firstPrice": product_sum_cart[0][i]['firstPrice'],
                                       "productId": product_sum_cart[0][i]['productId'],
                                       "productNum": product_sum_cart[0][i]['productNum'],
                                       "rePrice": product_sum_cart[0][i]['rePrice']
                                       }
                couponProductParamsList.append(couponProductParams)
        data = {"couponProductParamsList": couponProductParamsList, "conType": contype}
        res = requests.post(url=url, data=json.dumps(data), headers=heads)
        # print(res.json())
        couponList = jsonpath.jsonpath(res.json(), '$...mayUseCouponList')[0]
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        # print(couponList)
        try:
            coupon_code = couponList[0]['detailCode']
        except IndexError:
            print('该会员无优惠券')
        else:
            self.assertEqual(msg, '成功')
            return coupon_code


if __name__ == '__main__':
    t = CouponSelfCart()
    t.test_coupon_self_cart()

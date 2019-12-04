import json
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.mySql import Mysql
from Conf.url import url_order_put
from Lib.headers import heads
from MainInterface.front.address_isdefault import AddressDefault
from MainInterface.front.cart_list import CartList
from MainInterface.front.coupon_self_list import CouponSelfCart
from MainInterface.front.get_info import GetInfo
from MainInterface.front.put_price_cart import PutPrice


class OrderPutCart(unittest.TestCase):
    def test_order_put_cart(self):
        memberAddressId = AddressDefault().test_address_default()[0]
        # 获取商品信息
        product_sum_cart = CartList().test_cart_list()
        itemsList = []
        for i in range(0, len(product_sum_cart[0])):
            if product_sum_cart[0][i]['isSelected'] == 1:
                if 'skuId' in product_sum_cart[0][i] and product_sum_cart[0][i]['skuId'] != '':
                    items = {"productId": product_sum_cart[0][i]['productId'],
                             "quantity": product_sum_cart[0][i]['productNum'],
                             "skuId": product_sum_cart[0][i]['skuId']}
                else:
                    items = {"productId": product_sum_cart[0][i]['productId'],
                             "quantity": product_sum_cart[0][i]['productNum']}
                itemsList.append(items)
        productId_list = jsonpath.jsonpath(itemsList, '$..productId')
        # print(productId_list)
        # 获取运费模板 oracle
        provinceId = AddressDefault().test_address_default()[1]
        tmpl_id_list = []
        for i in range(len(productId_list)):
            oraDb = Oracle()
            sql = '''Select t.tmpl_id From pnt_product t Where t.product_id=:product_id'''
            tmpl_id = oraDb.queryBy(sql, {'product_id': productId_list[i]})[0][0]
            tmpl_id_list.append(tmpl_id)
        freight_list = []
        express_name = '普通快递'
        # 通过运费模板，获取其对应的运费信息 mysql
        for i in range(len(tmpl_id_list)):
            sqlDb = Mysql()
            sql = '''SELECT * FROM tb_express_template_item t 
        WHERE t.tmpl_id =(%s)  AND express_name =(%s) AND province_id =(%s)'''
            con_no = GetInfo().test_get_info()[2]
            sql_points = "update sp_points_member set points_available = '100' where con_no =%s" % '260053555'
            sqlDb.queryOne(sql_points)
            freight = sqlDb.queryBy(sql, (tmpl_id_list[i], express_name, provinceId))[0][6]
            freight_list.append(float('%.2f' % freight))
        freight_sum = 0
        for i in range(len(freight_list)):
            freight_sum = freight_sum + freight_list[i]
        coupon_code = CouponSelfCart().test_coupon_self_cart()
        data = {"remark": "", "isFreightFree": 0, "putType": 1, "couponCode": coupon_code,
                "paymentTypeid": "4",
                "itemsList": itemsList, "isJdexpress": 0, "memberAddressId": memberAddressId, "orderSource": "5",
                "isUsePoints": "1", "orderType": "1"}
        # print(data)
        url = url_order_put
        res = requests.post(url=url, data=json.dumps(data), headers=heads)
        print(res.json())
        orderTotal = jsonpath.jsonpath(res.json(), '$..orderTotal')[0]
        orderTotal_test = PutPrice().test_put_price() + freight_sum
        print(orderTotal_test, orderTotal)
        # self.assertEqual(orderTotal,)
        orderId = jsonpath.jsonpath(res.json(), '$..orderId')[0]
        try:
            self.assertEqual(orderTotal, orderTotal_test)
        except AssertionError:
            print('断言错误')
        else:
            return orderId

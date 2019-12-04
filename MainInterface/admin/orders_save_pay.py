# coding = utf-8
import json
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_orders_save_pay
from Lib.headers import heads1
from MainInterface.front.get_info import GetInfo

'''订单线下付款'''


class OrdersSavePay(unittest.TestCase):
    def test_orders_save_pay(self):
        oraDb = Oracle()
        con_no = GetInfo().test_get_info()[2]
        # con_no = '260053555'
        # print(con_no)
        sql = '''Select order_id From tld_orders  Where order_status_id = 1 and  con_no =:con_no'''
        try:
            order_id_list = oraDb.queryBy(sql, {'con_no': con_no})
        except IndexError:
            print('没新增订单了')
        else:
            for i in range(len(order_id_list)):
                print(order_id_list[i])
                url = url_orders_save_pay
                data1 = {"operateRemark": "测试", "orderId": order_id_list[i][0]}
                print(data1)
                res = requests.put(url, data=json.dumps(data1), headers=heads1)
                # print(res.json())
                msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
                self.assertEqual(msg1, '成功')

# if __name__ == '__main__':
#     t = OrdersSavePay()
#     t.test_orders_save_pay()

import unittest

import jsonpath
import requests

from Conf import url
from Conf.Oracle import Oracle
from Conf.url import url_oder_print
from Lib.headers import heads1
from MainInterface.front.get_info import GetInfo


class OrderPrint(unittest.TestCase):
    def test_order_print(self):
        oraDb = Oracle()
        con_no = GetInfo().test_get_info()[2]
        sql = '''Select order_id From tld_orders  Where order_status_id = 2 and  con_no =:con_no'''
        order_id_list = oraDb.queryBy(sql, {'con_no': con_no})
        if order_id_list:
            print(order_id_list)
            for i in range(len(order_id_list)):
                url = url_oder_print + order_id_list[i][0]
                print(url)
                res = requests.put(url, data=None, headers=heads1)
                print(res.json())
                msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
                self.assertEqual(msg, '成功')
        else:
            print('没有打印订单了')


if __name__ == '__main__':
    t = OrderPrint()
    t.test_order_print()

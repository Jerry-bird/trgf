import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_order_take
from Lib.headers import heads
from MainInterface.front.get_info import GetInfo

'''订单确认收货'''


class OrderTake(unittest.TestCase):
    def test_order_take(self):
        oraDb = Oracle()
        con_no = GetInfo().test_get_info()[2]
        sql = '''Select order_id From tld_orders  Where order_status_id = 6  and  con_no =:con_no'''
        order_id_list = oraDb.queryBy(sql, {'con_no': con_no})
        # print(order_id_list)
        if order_id_list:
            for i in range(len(order_id_list)):
                # print(order_id_list[i][0])
                url = url_order_take + order_id_list[i][0]
                # print(url)
                res = requests.put(url, data=None, headers=heads)
                msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
                self.assertEqual(msg, '成功')
        else:
            print('你已经没有配送中的订单了，亲')


if __name__ == '__main__':
    t = OrderTake()
    t.test_order_take()

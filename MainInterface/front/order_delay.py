import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_order_delay
from Lib.headers import heads
from MainInterface.front.get_info import GetInfo

'''延长收货'''


class OrderDelay(unittest.TestCase):
    def test_order_dalay(self):
        oraDb = Oracle()
        con_no = GetInfo().test_get_info()[2]
        sql = '''Select order_id From tld_orders  Where order_status_id = 6 And 
        delay_day Is Null and  con_no =:con_no'''
        order_id_list = oraDb.queryBy(sql, {'con_no': con_no})
        if order_id_list:
            for i in range(len(order_id_list)):
                print(order_id_list[i][0])
                url = url_order_delay + order_id_list[i][0]
                print(url)
                res = requests.put(url, data=None, headers=heads)
                msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
                self.assertEqual(msg, '成功')
        else:
            print('你现在没有配送中的订单哦，亲')


if __name__ == '__main__':
    t = OrderDelay()
    t.test_order_dalay()

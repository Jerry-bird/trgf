import json
import time
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_order_send
from Lib.headers import heads1
from MainInterface.front.get_info import GetInfo

'''订单发货'''


class OrderSend(unittest.TestCase):
    def test_order_send(self):
        url = url_order_send
        con_no = GetInfo().test_get_info()[2]
        oraDb = Oracle()
        sql_orderId = '''Select order_id From tld_orders  Where order_status_id = 5 and  con_no =:con_no'''
        order_id_list = oraDb.queryBy(sql_orderId, {'con_no': con_no})
        if order_id_list:
            for i in range(len(order_id_list)):
                order_Id = order_id_list[i][0]
                sql_split = '''Select split_id From tld_order_split  Where order_Id=:order_Id'''
                order_id_split = oraDb.queryBy(sql_split, {'order_Id': order_Id})
                ssrList = []
                # print(order_id_split)
                for s in range(len(order_id_split)):
                    # print(order_id_split[s][0])
                    # print(len(order_id_split))
                    ssr = {"expCompanyId": "27", "networkNo": "8E427F9A5E136D22E0530100007F464E",
                           "splitId": order_id_split[s][0], "waybillNo": int(time.time())}
                    ssrList.append(ssr)
                # print(ssrList)
                data = {"orderId": order_Id, "ssrList": ssrList}
                res = requests.put(url, data=json.dumps(data), headers=heads1)
                msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
                self.assertEqual(msg, '成功')
        else:
            print('你现在没有打印状态的订单了，亲')

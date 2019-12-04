import json
import time
import unittest

import requests
import jsonpath

from Conf.mySql import Mysql
from Conf.url import url_send_sms
from Lib.headers import heads
from MainInterface.front.get_info import GetInfo


class SendSms(unittest.TestCase):
    def test_send_sms(self):
        url = url_send_sms
        mobile = GetInfo().test_get_info()[8]
        data = {"flag": 1, "mobile": mobile, "operType": "5"}
        # print(data)
        res = requests.post(url=url, data=json.dumps(data), headers=heads)
        # print(res.json())
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        try:
            self.assertEqual(msg, '成功')
        except AssertionError:
            print('发送验证码失败')
        else:
            # 休息5秒，取验证码
            # time.sleep(5)
            sqlDb = Mysql()
            sendee = mobile
            sql_sms = '''select content from msg_log_sms   where sendee ='%s' order by update_time desc  limit 1''' % \
                      sendee
            sms = sqlDb.queryBy(sql_sms)[0][0]
            print(mobile)
            print('亲,你发送的验证码是：' + sms)
            return sms

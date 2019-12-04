import time
import unittest

import jsonpath
import requests

from Conf.url import url_performance_recalculation
from Lib.headers import heads1
from MainInterface.front.get_info import GetInfo


class Recalculation(unittest.TestCase):
    def test_performance_recalculation(self):
        # 佣金重算
        con_no = GetInfo().test_get_info()[2]
        print(con_no)
        url_recalculate = url_performance_recalculation + con_no
        res = requests.post(url=url_recalculate, data=None, headers=heads1)
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')
        print('等10秒，重算需要时间的')
        time.sleep(10)
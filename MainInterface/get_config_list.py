import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-sys/api-config-cache/list'


# 协议版本缓存

class ConfigList(unittest.TestCase):
    def test_get_config_list(self):
        res = requests.get(url, params=None, headers=heads)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        print(msg1)
        self.assertEqual(msg1, '成功')
        # oraDb = Oracle()
        # sql = """select * from   tld_orders  where con_no =: con_no """
        # msg2 = oraDb.queryBy(sql, {'con_no': '260053441'})
        # self.assertEqual(msg1, msg2)


if __name__ == '__main__':
    t = ConfigList()
    t.test_get_config_list()

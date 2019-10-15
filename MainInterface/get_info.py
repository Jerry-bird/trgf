import unittest

import jsonpath
import requests
from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-member/customer/info/get'


class GetInfo(unittest.TestCase):

    def test_get_info(self):
        res = requests.get(url, params=None, headers=heads)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        # print('我是msg1:'+msg1)
        self.assertEqual(msg1, '成功')
        con_id = jsonpath.jsonpath(res.json(), '$..conId')[0]
        return con_id


if __name__ == '__main__':
    t = GetInfo()
    t.test_get_info()

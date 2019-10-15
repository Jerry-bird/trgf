# coding = urt-8
import unittest

import jsonpath
import requests

from MainExecute.readConfig import ReadConfig
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-sys/operation-navigation/operation/list'
print(url)


class GetOperatiponList(unittest.TestCase):

    def test_get_operation_list(self):
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        print(msg1)
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = GetOperatiponList()
    t.test_get_operation_list()

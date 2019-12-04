# coding = urt-8
import unittest

import jsonpath
import requests

from Conf.url import url_operation_list
from Lib.headers import heads


class GetOperationList(unittest.TestCase):

    def test_get_operation_list(self):
        url = url_operation_list
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        print(msg1)
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = GetOperationList()
    t.test_get_operation_list()

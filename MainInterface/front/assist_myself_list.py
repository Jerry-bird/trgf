# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.url import url_assist_myList
from Lib.headers import heads

# url = ReadConfig().get_http('base_url') + '/ms-promotion/assist-free/myself/index'


class AssistMyselfList(unittest.TestCase):
    def test_assist_myself_list(self):
        url = url_assist_myList
        res = requests.get(url, params=None, headers=heads)
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')


if __name__ == '__main__':
    t = AssistMyselfList()
    t.test_assist_myself_list()

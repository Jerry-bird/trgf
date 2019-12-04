import json
import unittest

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_cart_insert
from Lib.headers import heads
from MainInterface.front.get_index_sku import IndexSku


class test1(unittest.TestCase):
    def test_cart_insert_sku(self):

            print(msg)
            self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = test1()
    t.test_cart_insert_sku()
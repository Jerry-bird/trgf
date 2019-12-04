# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.mySql import Mysql
from Conf.url import url_address_default
from MainInterface.front.get_info import GetInfo
from Lib.headers import heads

# url = ReadConfig().get_http('baseurl') + '/ms-order/member-address/address/isdefault'


class AddressDefault(unittest.TestCase):
    def test_address_default(self):
        url = url_address_default
        res = requests.get(url, params=None, headers=heads)
        # print(res.json())
        address_id = int(jsonpath.jsonpath(res.json(), '$..id')[0])
        provinceId = int(jsonpath.jsonpath(res.json(), '$..provinceId')[0])
        oraDb = Mysql()
        con_id = GetInfo().test_get_info()[0]
        sql = '''select * from member_address t where  is_default = '1'AND t.con_id =(%s)'''
        lists = oraDb.queryBy(sql, con_id)
        address_id_mysql = lists[0][0]
        self.assertEqual(address_id, address_id_mysql)
        # print(address_id)
        return address_id, provinceId


if __name__ == '__main__':
    t = AddressDefault()
    t.test_address_default()

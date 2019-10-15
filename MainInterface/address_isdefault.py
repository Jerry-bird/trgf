# coding = utf-8
import unittest

import jsonpath
import requests

from Conf.mySql import Mysql
from MainExecute.readConfig import ReadConfig
from MainInterface.get_info import GetInfo
from Lib.headers import heads

url = ReadConfig().get_http('baseurl') + '/ms-order/member-address/address/isdefault'


class AddressIsdefault(unittest.TestCase):
    def test_address_isdefault(self):
        res = requests.get(url, params=None, headers=heads)
        # print(res.json())
        address_id = int(jsonpath.jsonpath(res.json(), '$..id')[0])
        provinceId = int(jsonpath.jsonpath(res.json(), '$..provinceId')[0])
        # print(provinceId)
        # print(res.json())
        # print(address_id)
        oraDb = Mysql()
        con_id = GetInfo().test_get_info()
        sql = '''select * from member_address t where  is_default = '1'AND t.con_id =(%s)'''
        lists = oraDb.queryBy(sql, con_id)
        # print(lists)
        address_id_mysql = lists[0][0]
        # print(lists)
        self.assertEqual(address_id, address_id_mysql)
        # print(address_id)
        return address_id, provinceId


if __name__ == '__main__':
    t = AddressIsdefault()
    t.test_address_isdefault()

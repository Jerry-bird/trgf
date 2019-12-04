import unittest

import jsonpath
import requests

from Conf.url import url_get_info
from Lib.headers import heads


class GetInfo(unittest.TestCase):

    def test_get_info(self):
        url = url_get_info
        res = requests.get(url, params=None, headers=heads)
        # print(res.json())
        msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg1, '成功')
        # 会员ID
        con_id = jsonpath.jsonpath(res.json(), '$..conId')[0]
        # 会员类型
        conType = jsonpath.jsonpath(res.json(), '$..conType')[0]
        # 会员号
        con_no = jsonpath.jsonpath(res.json(), '$..conNo')[0]
        # 总佣金金额--提成
        balanceAmount = float('%.2f' % jsonpath.jsonpath(res.json(), '$..balanceAmount')[0])
        # 津贴总额 -- 竹妃津贴
        totalAllowanceHis = float('%.2f' % jsonpath.jsonpath(res.json(), '$..totalAllowanceHis')[0])
        # 奖励总额 -- 排行榜奖励
        totalAwardHis = float('%.2f' % jsonpath.jsonpath(res.json(), '$..totalAwardHis')[0])
        # 店铺返利总额--津贴
        shopAwardHis = float('%.2f' % jsonpath.jsonpath(res.json(), '$..shopAwardHis')[0])
        # print(balanceAmount, totalAllowanceHis, totalAwardHis, shopAwardHis)
        con_name = jsonpath.jsonpath(res.json(), '$..conName')[0]
        # 会员手机号，提现发送验证码
        mobile = jsonpath.jsonpath(res.json(), '$..mobile')[0]
        # print(mobile)
        return con_id, conType, con_no, balanceAmount, totalAllowanceHis, totalAwardHis, shopAwardHis, con_name, mobile


if __name__ == '__main__':
    t = GetInfo()
    t.test_get_info()

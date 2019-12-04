import unittest

import jsonpath
import requests

from Conf.url import url_commission_app
from Lib.headers import heads
from MainInterface.front.get_info import GetInfo


class CommissionApp(unittest.TestCase):
    def test_commission_app(self):
        url = url_commission_app
        res = requests.get(url=url, params=None, headers=heads)
        # print(res.json())
        # 当前可提现佣金-提成
        requestBalance = float('%.2f' % jsonpath.jsonpath(res.json(), '$..requestBalance')[0])
        # 竹妃津贴余额
        totalAllowance = float('%.2f' % jsonpath.jsonpath(res.json(), '$..totalAllowance')[0])
        # 奖励余额
        totalAward = float('%.2f' % jsonpath.jsonpath(res.json(), '$..totalAward')[0])
        # 店铺返利余额 - 津贴
        shopAwardAvailable = float('%.2f' % jsonpath.jsonpath(res.json(), '$..shopAwardAvailable')[0])
        # 推广费总额
        promotionFee = float('%.2f' % jsonpath.jsonpath(res.json(), '$..promotionFee')[0])
        # 引入个人信息接口中推广费各项总额数据，已变对推广费总额进行校验
        # 总佣金金额--提成
        balanceAmount = GetInfo().test_get_info()[3]
        # 津贴总额 -- 竹妃津贴
        totalAllowanceHis = GetInfo().test_get_info()[4]
        # 奖励总额 -- 排行榜奖励
        totalAwardHis = GetInfo().test_get_info()[5]
        # 店铺返利总额--津贴
        shopAwardHis = GetInfo().test_get_info()[6]
        promotionFee_test = balanceAmount + totalAllowanceHis + totalAwardHis + shopAwardHis
        self.assertEqual(promotionFee, promotionFee_test)
        # 可提取金额
        Commission = requestBalance + totalAllowance + totalAward + shopAwardAvailable
        # 申请中金额
        applying = float('%.2f' % jsonpath.jsonpath(res.json(), '$..applying')[0])
        # 已通过提现金额
        passed = float('%.2f' % jsonpath.jsonpath(res.json(), '$..passed')[0])
        # 最大提现总数
        maxAllowCount = jsonpath.jsonpath(res.json(), '$..maxAllowCount')[0]
        # 剩余可提现次数
        allowCount = jsonpath.jsonpath(res.json(), '$..allowCount')[0]
        # # 推广费总额-已通过金额-申请中金额
        # Commission_test = promotionFee - applying - passed
        # print(applying, passed, maxAllowCount, allowCount, Commission_test)
        # print(requestBalance, totalAllowance, totalAward, shopAwardAvailable, promotionFee, Commission)
        # print(balanceAmount, totalAllowanceHis, totalAwardHis, shopAwardHis, promotionFee_test)
        # print(Commission, applying, passed, allowCount)
        return Commission, allowCount, totalAllowance, requestBalance, shopAwardAvailable, totalAward


if __name__ == '__main__':
    t = CommissionApp()
    t.test_commission_app()

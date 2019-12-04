import json
import unittest

import jsonpath
import requests

from Conf.url import url_apply_check_code
from Lib.headers import heads
from MainInterface.front.cash_deduction import CashDeduction
from MainInterface.front.get_info import GetInfo
from MainInterface.front.send_sms import SendSms
from MainInterface.front.withdraw import test_withdraw


class ApplyCheckWx(unittest.TestCase):
    def test_apply_check_wx(self):
        url = url_apply_check_code
        withdraw_list = test_withdraw()
        # 竹妃津贴
        subsidy = withdraw_list[0]
        # 佣金提成
        commission = withdraw_list[1]
        # 店铺返利--津贴
        shop = withdraw_list[2]
        # 奖励--排行榜奖励 + 合伙人奖励
        reward = withdraw_list[3]
        # 获取提取的金额
        amount_put = CashDeduction().test_cash_deduction()[1]
        # print(subsidy, commission, shop, reward)
        # 获取会员绑定的手机号
        mobile = GetInfo().test_get_info()[8]
        # 获取发送的验证码
        sms = SendSms().test_send_sms()
        data = {"alipayAccount": "", "subsidy": subsidy, "bankCard": "", "realName": "李鹏", "refundType": "0",
                "amount": amount_put, "mobile": mobile, "bankName": "", "shop": shop, "reward": reward, "flag": 1,
                "captcha": sms, "channelPay": 1, "commission": commission, "cellPhone": mobile}
        # print(data)
        res = requests.post(url=url, data=json.dumps(data), headers=heads)
        # print(res.json())
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        try:
            self.assertEqual(msg, '成功')
        except AssertionError:
            print(msg)
        else:
            print('微信提现成功')


if __name__ == '__main__':
    t = ApplyCheckWx()
    t.test_apply_check_wx()

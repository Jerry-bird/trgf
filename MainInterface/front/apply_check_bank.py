import json
import unittest

import jsonpath
import requests

from Conf.url import url_apply_check_code
from Lib.headers import heads
from MainInterface.front.cash_deduction import CashDeduction
from MainInterface.front.get_info import GetInfo
from MainInterface.front.send_sms import SendSms
from MainInterface.front.use_bank import UseBank
from MainInterface.front.withdraw import test_withdraw


class ApplyCheckBank(unittest.TestCase):
    def test_apply_check_bank(self):
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
        # 获取银行卡的卡号，姓名，银行名称，银行卡绑定手机号
        bank_info_list = UseBank().test_use_bank()
        # 支付类型，自发or代付
        channelPay = bank_info_list[0]
        # 银行卡名称
        bank_name = bank_info_list[1]
        # 银行卡号
        bank_card = bank_info_list[4]
        # 真实姓名
        real_name = bank_info_list[3]
        # # 银行卡绑定手机号
        # mobile = bank_info_list[4]
        # 获取发送的短信验证码
        sms = SendSms().test_send_sms()
        # 获取发送验证码的手机
        cellphone = GetInfo().test_get_info()[8]
        # print(cellphone)
        # print(channelPay, bank_name, bank_card, real_name, mobile)
        data = {"alipayAccount": "", "subsidy": subsidy, "bankCard": bank_card, "realName": real_name,
                "refundType": "2", "amount": amount_put, "mobile": cellphone, "bankName": bank_name,
                "shop": shop, "reward": reward, "flag": 1,
                "captcha": sms, "channelPay": channelPay, "commission": commission, "cellPhone": cellphone}
        # print(data)
        res = requests.post(url=url, data=json.dumps(data), headers=heads)
        # print(res.json())
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        try:
            self.assertEqual(msg, '成功')
        except AssertionError:
            print(msg)
        else:
            print('银行卡提现成功')
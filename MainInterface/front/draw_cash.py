import unittest
import random

from MainInterface.front.account_info import test_account_info
from MainInterface.front.apply_check_bank import ApplyCheckBank
from MainInterface.front.apply_check_wx import ApplyCheckWx
from MainInterface.front.cash_deduction import CashDeduction


class DrawCash(unittest.TestCase):
    def test_draw_cash(self):
        amount_put = CashDeduction().test_cash_deduction()[1]
        bankWithdrawLower = test_account_info()
        print(amount_put)
        # print(amount_put, bankWithdrawLower)
        if amount_put <= bankWithdrawLower:
            apply_wx = ApplyCheckWx()
            apply_wx.test_apply_check_wx()
        else:
            num = random.randint(1, 100)
            if num % 2 == 1:
                apply_wx = ApplyCheckWx()
                apply_wx.test_apply_check_wx()
            else:
                apply_bank = ApplyCheckBank()
                apply_bank.test_apply_check_bank()

import unittest

from MainInterface.front.cash_deduction import CashDeduction
from MainInterface.front.commission_app import CommissionApp



def test_withdraw():
    amount_put = CashDeduction().test_cash_deduction()[1]
    print(amount_put)
    # 引入竹妃津贴
    totalAllowance = CommissionApp().test_commission_app()[2]
    # 引入佣金--提成
    requestBalance = CommissionApp().test_commission_app()[3]
    # 引入店铺返利---津贴
    shopAwardAvailable = CommissionApp().test_commission_app()[4]
    # 奖励 --合伙人奖励和排行榜奖励
    totalAward = CommissionApp().test_commission_app()[5]
    # print(totalAllowance, requestBalance, shopAwardAvailable, totalAward)
    if amount_put < totalAllowance:
        subsidy = amount_put
        commission = 0
        shop = 0
        reward = 0
    elif 0 <= amount_put - totalAllowance <= requestBalance:
        subsidy = totalAllowance
        commission = float('%.2f' % (amount_put - totalAllowance))
        shop = 0
        reward = 0
    elif 0 < amount_put - totalAllowance - requestBalance <= shopAwardAvailable:
        subsidy = totalAllowance
        commission = requestBalance
        shop = float('%.2f' % (amount_put - totalAllowance - requestBalance))
        reward = 0
    else:
        subsidy = totalAllowance
        commission = requestBalance
        shop = shopAwardAvailable
        reward = float('%.2f' % (amount_put - totalAllowance - requestBalance - shopAwardAvailable))
    return subsidy, commission, shop, reward

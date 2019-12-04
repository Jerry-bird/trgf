import random
import unittest

from Conf.Oracle import Oracle
from MainInterface.front.get_info import GetInfo


class GenerateAward(unittest.TestCase):
    """生成提成数据"""

    def generate_commission(self):
        # 从订单表所有的order_status_id = 7的订单中随机选取其中一个订单的订单ID
        oraDb = Oracle()
        sql_orderId = '''Select order_id From tld_orders  Where  order_status_id = 7 And  Rownum <= 10'''
        orderIdList = oraDb.queryBy(sql_orderId)
        order_Id = random.sample(orderIdList, 1)[0][0]
        # 选取的随机订单修改数据，以增加提成
        referee_no = GetInfo().test_get_info()[2]
        referee_id = GetInfo().test_get_info()[0]
        Level_Up1_Commission = random.randint(1, 100)
        # print(Level_Up1_Commission, type(order_Id), referee_no, referee_id, order_Id)
        sql_commission = "Update Tld_Orders Set Level_Up1_Commission =%s ,referee_id ='%s'," \
                         "referee_no =%s Where Order_Id ='%s'" % \
                         (Level_Up1_Commission, referee_id, referee_no, order_Id)
        # print(sql_commission)
        ora_commission = oraDb.query(sql_commission)

    '''生成津贴数据'''

    def generate_shop_comm(self):
        # 从津贴返利表所有的order_status_id = 7的订单中随机选取其中一个订单的订单ID
        oraDb = Oracle()
        con_no = GetInfo().test_get_info()[2]
        sql_orderId = '''Select order_id From TLD_ORDER_SHOP_AWARD  Where  order_stats_id = 7 and 
        con_no!=:con_no And  Rownum <= 10'''
        orderIdList = oraDb.queryBy(sql_orderId, {'con_no': con_no})
        order_Id = random.sample(orderIdList, 1)[0][0]
        print(order_Id)
        # 选取的随机津贴订单修改数据，以增加津贴
        shop_con_id = GetInfo().test_get_info()[0]
        shop_con_no = GetInfo().test_get_info()[2]
        shop_comm = random.randint(1, 100)
        sql_comm = "Update TLD_ORDER_SHOP_AWARD Set shop_comm =%s ,shop_con_id ='%s' ," \
                   "shop_con_no ='%s' Where order_id ='%s'" \
                   % (shop_comm, shop_con_id, shop_con_no, order_Id)
        ora_comm = oraDb.query(sql_comm)

    '''生成竹妃津贴'''

    def generate_allowance(self):
        # 从竹妃津贴表中随机选取10条数据，取出ID
        oraDb = Oracle()
        con_no = GetInfo().test_get_info()[2]
        con_id = GetInfo().test_get_info()[0]
        sql_orderId = '''Select order_id From TLD_ALLOWANCE_STATS  Where  Rownum <= 10 and con_no!=:con_no'''
        orderIdList = oraDb.queryBy(sql_orderId, {'con_no': con_no})
        order_Id = random.sample(orderIdList, 1)[0][0]
        allowance = random.randint(1, 10)
        sql_allowance = "Update TLD_ALLOWANCE_STATS Set con_id ='%s' ,con_no =%s , allowance =%s Where order_id ='%s' " \
                        % (con_id, con_no, allowance, order_Id)
        ora_allowance = oraDb.query(sql_allowance)
    

if __name__ == '__main__':
    t = GenerateAward()
    # t.generate_commission()
    # t.generate_shop_comm()
    t.generate_allowance()

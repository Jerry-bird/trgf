import unittest

from Conf.Oracle import Oracle
from Lib.get_agent import GetAgent
from Lib.get_product_info import GetProductInfo
from Lib.points_share import PointsShare
from Lib.product_price_totle import PriceTotal


class CommissionCount(unittest.TestCase):
    def test_commission_count(self):
        orderId = '63a15c7c26a848f48682017f30a6af00'
        # 获取价格列表
        product_price_list = GetProductInfo(orderId).get_product_price()
        # 获取数量列表
        product_num_list = GetProductInfo(orderId).get_product_num()
        # 获取商品ID列表
        product_list = GetProductInfo(orderId).get_product_id()
        # 获取各个商品计算总额
        product_price_sum_list = PriceTotal(product_price_list, product_num_list).price_total()[0]
        # 获取商品总价格，用以传给积分分摊计算的方法
        product_price_total = PriceTotal(product_price_list, product_num_list).price_total()[1]
        # print(product_price_list, product_num_list, product_price_sum_list, product_price_total)
        # 获取使用积分，用以传给积分分摊计算的方法
        pointsAmount = GetProductInfo(orderId).get_points_Amounts()
        points_share_list = PointsShare(product_price_sum_list, product_price_total, pointsAmount).points_share()
        # print(points_share_list)
        # 计算佣金时，是用原价减去积分分摊金额作为价格来算提成的
        real_price_list = []
        sale_price_list = GetProductInfo(orderId).get_sale_price()
        for i in range(len(product_price_sum_list)):
            real_price_list.append(float('%.2f' % (sale_price_list[i] - points_share_list[i])))
        # print(real_price_list)
        # 获取每个商品的首购提成比例和复购提成比例
        before_agent1 = []
        after_agent1 = []
        for i in range(len(product_list)):
            before_agent1.append(GetAgent(product_list[i]).get_agent()[0] / 100)
            after_agent1.append(GetAgent(product_list[i]).get_agent()[1] / 100)
        # print(before_agent1, after_agent1)
        # 获取该订单是否是重销单
        oraDb = Oracle()
        sql_reorder = '''Select is_reorder From tld_orders  Where order_id ='%s' ''' % orderId
        # print(sql_reorder)
        is_reorder = oraDb.queryBy(sql_reorder)[0][0]
        # 获取每个商品的提成
        commission_count_list = []
        if is_reorder == 0:
            for i in range(len(product_list)):
                commission_count_list.append(float('%.2f' % (real_price_list[i] * before_agent1[i])))
        else:
            for i in range(len(product_list)):
                commission_count_list.append(float('%.2f' % (real_price_list[i] * after_agent1[i])))
        # print(commission_count_list)
        # 计算此订单产生的提成总和
        commission_count = 0
        for i in range(len(commission_count_list)):
            commission_count = commission_count + float('%.2f' % commission_count_list[i])
        # print(commission_count)

        sql_promotion_fee = '''Select promotion_fee From tld_orders  Where order_id ='%s' ''' % orderId
        promotion_fee = oraDb.queryBy(sql_promotion_fee)[0][0]
        try:
            self.assertEqual(promotion_fee, commission_count)
        except AssertionError:
            print('提成计算错误')
        else:
            print('提成计算正确')
        return commission_count


if __name__ == '__main__':
    t = CommissionCount()
    t.test_commission_count()

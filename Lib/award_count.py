import math
import unittest

import numpy as np

from Conf.Oracle import Oracle
from Lib.get_params_list import GetParamsList
from Lib.get_product_info import GetProductInfo
from Lib.get_shop_params import GetShopParams
from Lib.points_share import PointsShare
from Lib.product_price_totle import PriceTotal
from Lib.query_post_no import QueryPostNo
from Lib.query_referee import QueryReferee


class AwardCount(unittest.TestCase):
    def test_get_award_count(self):
        orderId = '78c88aa2843143e0931578d3121916f2'
        con_no = '260053555'
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
        print(real_price_list)
        # 获取会员的推荐人信息
        con_no_list = QueryReferee(con_no).query_referee()
        # 获取有效的推荐人信息和岗位信息
        post_no_list_new = QueryPostNo(con_no_list).query_post_no()[0]
        con_no_list_new = QueryPostNo(con_no_list).query_post_no()[1]
        print(post_no_list_new, con_no_list_new)
        # 根据岗位信息和订单中商品，获取推荐人对应的津贴比例
        percent_lists_new = GetShopParams(post_no_list_new, product_list).get_shop_params()[0]
        repercent_lists_new = GetShopParams(post_no_list_new, product_list).get_shop_params()[1]
        # print(percent_lists_new, repercent_lists_new)
        # 根据需求规则，津贴是层层扣减的
        percent_list_new_all = GetParamsList(percent_lists_new, repercent_lists_new).get_percent_list()
        repercent_list_new_all = GetParamsList(percent_lists_new, repercent_lists_new).get_repercent_list()
        print(percent_list_new_all, repercent_list_new_all)
        # 获取该订单是否是重销单
        oraDb = Oracle()
        sql_reorder = '''Select is_reorder From tld_orders  Where order_id ='%s' ''' % orderId
        # print(sql_reorder)
        is_reorder = oraDb.queryBy(sql_reorder)[0][0]
        list2 = []
        list3 = []
        # 根据是否重销单判断使用哪个比例
        # 计算每个商品的每个层级津贴时，只舍不进
        if is_reorder == 0:
            for i in range(len(percent_list_new_all)):
                for s in range(len(percent_list_new_all[i])):
                    ss = math.floor(percent_list_new_all[i][s] * real_price_list[i]) / 100
                    list2.append(ss)
                    # print(list2)
            for i in range(0, len(list2), len(percent_list_new_all[1])):
                list3.append(list2[i:i + len(percent_list_new_all[1])])
            # print(list3)
        else:
            for i in range(len(repercent_list_new_all)):
                for s in range(len(repercent_list_new_all[i])):
                    ss = math.floor(repercent_list_new_all[i][s] * real_price_list[i]) / 100
                    # ss = repercent_list_new_all[i][s] * real_price_list[i] / 100
                    list2.append(ss)
                    # print(list2)
            for i in range(0, len(list2), len(repercent_list_new_all[1])):
                list3.append(list2[i:i + len(repercent_list_new_all[1])])
            # print(list3)
        award = 0
        for i in range(len(list3)):
            award = award + np.array(list3[i])
        print(award)


if __name__ == '__main__':
    t = AwardCount()
    t.get_award_count()

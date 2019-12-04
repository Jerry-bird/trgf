class PointsShare:
    def __init__(self, product_price_sum_list, product_price_total, pointsAmount):
        self.product_price_sum_list = product_price_sum_list
        self.product_price_total = product_price_total
        self.pointsAmount = pointsAmount

    def points_share(self):
        # 计算商品的分摊积分
        points_share_list = []
        for i in range(len(self.product_price_sum_list) - 1):
            points_share = float('%.2f' % (self.product_price_sum_list[i] *
                                           self.pointsAmount / self.product_price_total))
            points_share_list.append(points_share)

        # 由于四舍五入会导致总和大于积分抵现金额，所以最后一个商品的分摊积分折现只能有总和 减去前面所有的积分折现之和
        points_share_part = 0
        for i in range(len(points_share_list)):
            points_share_part = points_share_part + points_share_list[i]
        points_share_list.append(float('%.2f' % (self.pointsAmount - points_share_part)))
        # print(points_share_list)
        return points_share_list


# product_price_sum_list = [71.2, 79.2, 55.2, 63.2, 79.2]
# # product_price_total = 348.0
# # pointsAmount = 2
# #
# # t = PointsShare(product_price_sum_list, product_price_total, pointsAmount)
# # t.points_share()

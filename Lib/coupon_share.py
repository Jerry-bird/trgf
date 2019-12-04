"""计算佣金不考虑优惠券分摊"""


class CouponShare:
    def __init__(self, product_price_sum_list, product_num_list, couponAmount):
        self.product_price_sum_list = product_price_sum_list
        self.product_num_list = product_num_list
        self.couponAmount = couponAmount

    def coupon_list(self):
        # 计算商品的分摊优惠券
        coupon_share_list = []
        for i in range(len(self.product_price_sum_list) - 1):
            coupon_share = float('%.2f' % (self.product_price_sum_list[i] *
                                           self.couponAmount / self.product_price_total))
            coupon_share_list.append(coupon_share)

        # 由于四舍五入会导致总和大于优惠券金额，所以最后一个商品的分摊优惠券抵现只能用总和 减去前面所有的优惠券抵现之和
        coupon_share_part = 0
        for i in range(len(coupon_share_list)):
            coupon_share_part = coupon_share_part + coupon_share_list[i]
        coupon_share_list.append(float('%.2f' % (self.couponAmount - coupon_share_part)))
        return coupon_share_list

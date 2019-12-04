class PriceTotal:
    def __init__(self, product_price_list, product_num_list):
        self.product_price_list = product_price_list
        self.product_num_list = product_num_list

    def price_total(self):
        # 计算订单内各个商品的价格
        product_price_sum_list = []
        for i in range(len(self.product_price_list)):
            product_price_sum = self.product_price_list[i] * self.product_num_list[i]
            product_price_sum_list.append(product_price_sum)

        # 计算商品的总价
        product_price_total = 0
        for i in range(len(product_price_sum_list)):
            product_price_total = product_price_total + float('%.2f' % product_price_sum_list[i])
        return product_price_sum_list, product_price_total
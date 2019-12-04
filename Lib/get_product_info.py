import requests
import jsonpath

from Conf.Oracle import Oracle
from Conf.url import url_order_info
from Lib.headers import heads

'''获取订单的商品信息，用作计算佣金'''


class GetProductInfo:
    def __init__(self, order_id):
        self.order_id = order_id
        url = url_order_info + self.order_id
        res = requests.get(url, params=None, headers=heads)
        self.itemsList = jsonpath.jsonpath(res.json(), '$..itemsList')[0]
        self.pointsAmount = jsonpath.jsonpath(res.json(), '$..pointsAmount')[0]

    def get_product_id(self):
        product_list = []
        # for i in range(len(self.itemsList)):
        #     product_id = self.itemsList[i]['productId']
        #     product_list.append(product_id)
        # return product_list
        oraDb = Oracle()
        sql_product_id = ''' Select product_id From Tld_Order_Items   Where  Order_Id ='%s' ''' % self.order_id
        product_list_part = oraDb.queryBy(sql_product_id)
        for i in range(len(product_list_part)):
            product_list.append(product_list_part[i][0])
        # print(product_list)
        return product_list

    def get_product_price(self):
        product_price_list = []
        # for i in range(len(self.itemsList)):
        #     product_price = self.itemsList[i]['actualAmount']
        #     product_price_list.append(product_price)
        # # print(product_price_list)
        # return product_price_list
        oraDb = Oracle()
        sql_product_price = ''' Select actual_amount From Tld_Order_Items   Where  Order_Id ='%s' ''' % self.order_id
        product_price_list_part = oraDb.queryBy(sql_product_price)
        for i in range(len(product_price_list_part)):
            product_price_list.append(product_price_list_part[i][0])
        # print(product_price_list)
        return product_price_list

    def get_product_num(self):
        product_num_list = []
        for i in range(len(self.itemsList)):
            product_num = self.itemsList[i]['quantity']
            product_num_list.append(product_num)
        return product_num_list

    def get_points_Amounts(self):
        # print(self.pointsAmount)
        return self.pointsAmount

    def get_sale_price(self):
        sale_price_list = []
        oraDb = Oracle()
        sql_sale_price = ''' Select sale_price From Tld_Order_Items   Where  Order_Id ='%s' ''' % self.order_id
        sale_price_list_part = oraDb.queryBy(sql_sale_price)
        for i in range(len(sale_price_list_part)):
            sale_price_list.append(float('%.2f' % sale_price_list_part[i][0]))
            # print(type(sale_price_list[i]))
        return sale_price_list


s = GetProductInfo('63a15c7c26a848f48682017f30a6af00')
s.get_product_id()
# b = s.get_points_Amounts()

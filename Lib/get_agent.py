from Conf.Oracle import Oracle
from Lib.get_product_info import GetProductInfo

'''获取商品的提成比例信息，用以计算佣金'''


class GetAgent:
    def __init__(self, product_id):
        self.product_id = product_id

    def get_agent(self):
        oraDb = Oracle()
        sql_agent = " Select befor_agent1,after_agent1 From pnt_product  Where product_id = '%s' " % self.product_id
        # print(sql_agent)
        before_agent1 = oraDb.queryBy(sql_agent)[0][0]
        after_agent1 = oraDb.queryBy(sql_agent)[0][1]
        # print(agent)
        return before_agent1, after_agent1


product_list = GetProductInfo('63a15c7c26a848f48682017f30a6af00').get_product_id()
# print(product_list)
for i in range(len(product_list)):
    product_id = product_list[i]
    s = GetAgent(product_id)
    s.get_agent()

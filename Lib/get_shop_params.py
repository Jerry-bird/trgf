from Conf.Oracle import Oracle


class GetShopParams:
    def __init__(self, post_no_list_new, product_list):
        self.post_no_list_new = post_no_list_new
        self.product_list = product_list

    def get_shop_params(self):
        oraDb = Oracle()
        percent_list = []
        repercent_list = []
        percent_lists_new = []
        repercent_lists_new = []
        for i in range(len(self.product_list)):
            for s in range(len(self.post_no_list_new)):
                sql_get_shop = '''Select percent, repercent From TLD_SHOP_PNT_PARMS t 
                Where t.product_id = '%s' And post_no = '%s' ''' \
                               % (self.product_list[i], self.post_no_list_new[s])
                percent = oraDb.queryBy(sql_get_shop)[0][0]
                repercent = oraDb.queryBy(sql_get_shop)[0][1]
                percent_list.append(percent)
                repercent_list.append(repercent)
        # print(percent_list)
        for i in range(0, len(percent_list), len(self.post_no_list_new)):
            percent_lists_new.append(percent_list[i:i + len(self.post_no_list_new)])
        # print(percent_lists_new)
        for i in range(0, len(repercent_list), len(self.post_no_list_new)):
            repercent_lists_new.append(repercent_list[i:i + len(self.post_no_list_new)])
        # print(repercent_lists_new)
        return percent_lists_new, repercent_lists_new


# post_no_list_new = ['014', '013', '0121', '012', '011']
# product_list = ['BFD2C74AEBD147FA9B37409DBCA3FF07', 'BB5B19EEA60A42E9817406226B37B561',
#                 'BFD2C74AEBD147FA9B37409DBCA3FF07', 'BFD2C74AEBD147FA9B37409DBCA3FF07']
# GetShopParams(post_no_list_new, product_list).get_shop_params()

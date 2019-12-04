from Conf.Oracle import Oracle
from Lib.set_award import set_award


class QueryPostNo:
    def __init__(self, con_no_list):
        self.con_no_list = con_no_list
    '''根据上级会员号获取对应的岗位信息'''
    def query_post_no(self):
        post_no_list = []
        post_no_list_new = []
        con_no_list_new = []
        for i in range(len(self.con_no_list)):
            oraDb = Oracle()
            sql_post = '''Select post_no From TLD_SHOP_AWARD_CONTRACT  Where status =1  
            And  con_no = %s ''' % self.con_no_list[i]
            # print(len(self.con_no_list))
            # print(sql_post)
            post_no = oraDb.queryBy(sql_post)[0][0]
            # print(post_no)
            # 去除失效的岗位会员，然后根据岗位信息去重，得到返津贴的岗位信息及会员信息
            if post_no is None:
                break
            else:
                post_no_list.append(post_no)
                for s in post_no_list:
                    if s not in post_no_list_new:
                        post_no_list_new.append(post_no)
                        con_no_list_new.append(self.con_no_list[i])
        # print(post_no_list_new, con_no_list_new)
        # print(post_no)
        return post_no_list_new, con_no_list_new


# con_no_list = ['260053744', '260053634', '260053555', '260053741', '260053742', '260053743']
# QueryPostNo(con_no_list).query_post_no()

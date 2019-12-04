from Conf.Oracle import Oracle


class QueryReferee:
    def __init__(self, con_no):
        self.con_no = con_no

    def query_referee(self):
        oraDb = Oracle()
        con_no_list = []
        for i in range(100):
            sql = '''Select referee_no From bas_customer  Where con_no = '%s' ''' % self.con_no
            self.con_no = oraDb.queryBy(sql)[0][0]
            # 若上级为空，则停止
            if self.con_no is None:
                break
            else:
                con_no_list.append(self.con_no)
            # print(self.con_no)
        # print(con_no_list)
        return con_no_list


# con_no = '260053555'
# QueryReferee(con_no).query_referee()
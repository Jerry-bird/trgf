# coding = urf-8
from Conf.Oracle import Oracle
from MainInterface.index_all_list import GetList


class GetTmplId(object):
    def get_tmpl_id(self):
        product_id = GetList().test_index_list()[0]
        oraDb = Oracle()
        sql = '''Select t.tmpl_id From pnt_product t Where t.product_id=:product_id'''
        lists = oraDb.queryBy(sql, {'product_id': product_id})[0][0]
        # print(lists)
        return lists


if __name__ == '__main__':
    t = GetTmplId()
    t.get_tmpl_id()

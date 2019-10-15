# coding = utf-8
from Conf.mySql import Mysql
from MainInterface.address_isdefault import AddressIsdefault
from MainInterface.tmpl_id import GetTmplId


class GetFreight(object):
    def get_freight(self):
        tmpl_id = GetTmplId().get_tmpl_id()
        # print(tmpl_id)
        oraDb = Mysql()
        provinceId = AddressIsdefault().test_address_isdefault()[1]
        # 　　print(provinceId)
        express_name = '普通快递'
        express_name_jd = '京东快递'
        sql = '''SELECT * FROM tb_express_template_item t 
        WHERE t.tmpl_id =(%s)  AND express_name =(%s) AND province_id =(%s) '''
        lists1 = oraDb.queryBy(sql, (tmpl_id, express_name, provinceId))[0][6]
        lists2 = oraDb.queryBy(sql, (tmpl_id, express_name_jd, provinceId))[0][6]
        return lists1, lists2


if __name__ == '__main__':
    t = GetFreight()
    t.get_freight()

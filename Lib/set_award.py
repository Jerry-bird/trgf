from Conf.Oracle import Oracle
from MainExecute.readConfig import ReadConfig


def set_award():
    oraDb = Oracle()
    con_14 = ReadConfig().get_con('con_14')
    con_13 = ReadConfig().get_con('con_13')
    con_121 = ReadConfig().get_con('con_121')
    con_12 = ReadConfig().get_con('con_12')
    con_11 = ReadConfig().get_con('con_11')
    sql_set = '''Update  TLD_SHOP_AWARD_CONTRACT  Set status = 1 Where con_no In (%s,%s,%s,%s,%s)''' % (
        con_14, con_13, con_121, con_12, con_11)
    oraDb.query(sql_set)


set_award()

from Conf.mySql import Mysql
from MainInterface.front.get_info import GetInfo


def get_points():
    # 获取会员的可用积分
    oraDb = Mysql()
    con_id = GetInfo().test_get_info()[0]
    # print(con_id)
    sql = '''select points_available from sp_points_member where con_id =(%s) '''
    points_available = float(oraDb.queryBy(sql, con_id)[0][0])
    # print(float(points_available))
    # print(type(float(points_available)))

    # 获取积分抵扣比例
    name = 'points_worth'
    sql = '''select value from sys_dict  t where  name = (%s)'''
    value = float(oraDb.queryBy(sql, name)[0][0])
    # print(float(value))
    # print(type(float(value)))

    # 计算抵扣金额
    amountAvailable = points_available / value
    return points_available, value


get_points()

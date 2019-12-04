from Conf.mySql import Mysql


def test():
    sqlDb = Mysql()

    sql = '''select * from sp_points_member where con_no=(%s)'''
    s = sqlDb.queryBy(sql, con_no)
    print(points)


test()

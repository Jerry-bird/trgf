# coding=utf-8

import pymysql

host = '192.168.1.94'
port = 3306
user = 'db_user01'
password = 'u#f*dR3erd'
db = 'admin'


class Mysql(object):
    """  oracle db operator  """

    def __init__(self):
        self._conn = pymysql.connect(host='192.168.1.94', port=3306, user='db_user01', password='u#f*dR3erd',
                                     db='admin',
                                     charset='utf8')
        self.cursor = self._conn.cursor()

    def queryTitle(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        colNames = []
        selectResultList = self.cursor.description
        for i in range(0, len(selectResultList)):
            # colNames.append(self.cursor.description[i][0])
            return selectResultList[i]

        return colNames

    # query methods
    def queryAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def queryOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def queryBy(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def insertBatch(self, sql, nameParams=[]):
        """batch insert much rows one time,use location parameter"""
        self.cursor.prepare(sql)
        self.cursor.executemany(None, nameParams)
        self.commit()

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()

        if hasattr(self, '_conn'):
            self._conn.close()


# def test1():
#     sql = """select * from   tld_orders  where con_no =: con_no """
#     oraDb = Oracle()
#
#     # fields = oraDb.queryTitle(sql, {'order_no': '2019092450000018'})
#     # print(fields)
#
#     print(oraDb.queryBy(sql, {'con_no': '260053441'}))


if __name__ == '__main__':
    con_no = '260053499'
    sql = '''select * from member_address t where t.con_no =(%s)'''
    print(sql)
    oraDb = Mysql()
    print(oraDb.queryBy(sql, con_no))

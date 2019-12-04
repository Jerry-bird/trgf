# coding:utf-8

import cx_Oracle

userName = 'cd_release'
password = 'cd_release'
host = '192.168.1.26'
instance = 'vellgo'


class Oracle(object):

    # 对oracle操作

    def __init__(self):
        self._conn = cx_Oracle.connect("%s/%s@%s/%s" % (userName, password, host, instance))
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
        self._conn.commit()
        return self.cursor.fetchone()

    def queryBy(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def query(self, sql):
        self.cursor.execute(sql)
        self._conn.commit()

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
    sql = """select * from   tld_orders  where con_no =: con_no """
    oraDb = Oracle()
    print(oraDb.queryBy(sql, {'con_no': '260053441'}))

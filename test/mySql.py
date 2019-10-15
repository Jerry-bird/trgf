# coding=utf-8
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='192.168.1.94', port=3306, user='db_user01', password='u#f*dR3erd', db='admin',
                       charset='utf8')

# 使用cursor()方法创建一个游标对象
cursor = conn.cursor()

# 使用execute()方法执行SQL查询
# id = '4'
# cursor.execute('SELECT * FROM  pss_jd_goods_stock t where t.id = %s', id)

cursor.execute('select * from pss_jd_goods_stock')

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

# 使用fetchall()遍历获取查询结果
selectResultList = cursor.fetchall()

for i in range(len(selectResultList)):
    print(selectResultList[i])
# 打印
# print(data)
# print('database version: %s' % (data,))

# SQL语句：向数据表中插入数据
sql = """INSERT INTO sys_bank(id,bank_code,bank_name,bg_url,status,create_by,update_by)
         VALUES ('200', 'cs1', '测试1', 'http://photo.vellgo.com.cn/images/bank/1533691528210.png', '1','trgf','trgf')"""
# SQL语句：更新数据库中的数据
sql1 = "UPDATE sys_bank SET id = '201' WHERE id ='200'"
# SQL语句：删除数据库中的数据
sql2 = "delete from  sys_bank where id = '201'"
# 异常处理
try:
    # 执行SQL语句
    cursor.execute(sql)
    print('插入成功')
    cursor.execute(sql1)
    print('更新成功')
    cursor.execute(sql2)
    print('删除成功')
    # 提交事务到数据库执行
    conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
except:
    # 如果发生错误则执行回滚操作
    conn.rollback()
    print('sql有问题')
# 关闭数据库连接
conn.close()

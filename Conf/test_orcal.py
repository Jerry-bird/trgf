import cx_Oracle

conn = cx_Oracle.connect('cd_release/cd_release@192.168.1.26:1521/vellgo')

# con1 = cx_Oracle.connect('cd_release', 'cd_release', '192.168.1.26:1521/vellgo')
dsn = cx_Oracle.makedsn('192.168.1.26', 1521, 'vellgo')
cursor = conn.cursor()
cursor.execute('select * from pnt_brand')

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

# 使用fetchall()遍历获取查询结果
selectResultList = cursor.fetchall()

for i in range(len(selectResultList)):
    print(selectResultList[i])

# print(data)
# print(selectResultList)

sql = 'select * from  pnt_brand  where c_index =99'

try:
    # 执行SQL语句
    cursor.execute(sql)
    print('插入成功')
    # cursor.execute(sql1)
    # print('更新成功')
    # cursor.execute(sql2)
    # print('删除成功')
    # 提交事务到数据库执行
    conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
except:
    # 如果发生错误则执行回滚操作
    conn.rollback()
    print('sql有问题')
# 关闭数据库连接
conn.close()

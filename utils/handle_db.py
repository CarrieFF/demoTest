# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_db.py
@IDE ：PyCharm
@Time ： 2022-07-20 20:26
"""
import pymysql

# 1. 创建链接
dbconnect = pymysql.connect(host='', port='', user='', password='', database='')
# 2. 获取游标
cursor = dbconnect.cursor()
# 3. 执行sql语句
sql = "select * from user where userName='小明'"
cursor.execute(sql)
# 4. 获取返回结果
result = cursor.fetchall()  # cursor.fetchone() 返回一条结果 all 返回所有结果
# 5. 关闭游标，关闭链接；
cursor.close()
dbconnect.close()


class DBConnection:
    def __init__(self, host='host', port='port', user='user', password='password', database='database'):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    # 查询方法
    def select(self, sql, many=True):
        self.cursor.execute(sql)
        if many:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()

    def handelSql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as error:
            self.db.rollback()
            print(f'mysqlDB error {error}')
            raise error
        self.db.commit()

    # 增加操作
    def insert(self, sql):
        self.handelSql(sql)

    # 修改操作
    def update(self, sql):
        self.handelSql(sql)

    # 删除操作
    def delete(self, sql):
        self.handelSql(sql)

    # 关闭游标和链接
    def exit(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    dbconnect = DBConnection()
    sql = "select * from user where userName='冉冉'"
    res = dbconnect.select(sql)
    dbconnect.exit()

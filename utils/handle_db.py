# -*- coding: utf-8 -*-
"""
@Auth ： Carrie
@File ：handle_db.py
@IDE ：PyCharm
@Time ： 2022-07-20 20:26
"""
import pymysql
from utils.handle_ini import conf
from utils.handle_loguru import log


class DBConnection:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=conf.get_str("mysql", "host"),
                                        user=conf.get_str("mysql", "user"),
                                        password=conf.get_str("mysql", "password"),
                                        port=conf.get_int("mysql", "port"),
                                        db=conf.get_str("mysql", "db"),
                                        charset="utf8")
            # 创建游标
            self.cursor = self.conn.cursor()
        except pymysql.err.OperationalError as e:
            log.info(e)
            raise e

    # 查询方法
    def select(self, sql, many=True):
        self.cursor.execute(sql)
        if many:
            result = self.cursor.fetchall()  # 返回所有的结果
        else:
            result = self.cursor.fetchone()  # 返回查到的第一条数据

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

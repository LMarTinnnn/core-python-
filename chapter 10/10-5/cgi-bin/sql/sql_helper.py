#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from config_user import table_name, db_path


class DataBase(object):
    def __init__(self):
        self.table_name = table_name
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.create()

    def create(self):
        sql_create = "CREATE TABLE IF NOT EXISTS %s (name TEXT, email TEXT, password TEXT)" % self.table_name
        self.cur.execute(sql_create)
        self.conn.commit()

    def insert(self, name, email, password):
        sql_insert = 'INSERT INTO %s VALUES(?,?,?)' % self.table_name
        data = (name, email, password)
        self.cur.execute(sql_insert, data)
        self.conn.commit()

    def get_info(self, name='', email='', key_only=False):
        if name:
            sql_select = 'SELECT name, password FROM %s WHERE name=?' % self.table_name
            self.cur.execute(sql_select, (name,))  # !!!!参数必须传tuple
            info = self.cur.fetchone()
        else:  # 用email查
            sql_select = 'SELECT name, password FROM %s WHERE email=?' % self.table_name
            self.cur.execute(sql_select, (email,))
            info = self.cur.fetchone()

        if info:
            key = str(info[1]) + 'salt'
            return key if key_only else (str(info[0]), key)  # !!!这里不用括号扩起来会有bug哦
        else:
            return None if key_only else (None, None)

    def exist_name(self, name):  # 存在为真 反之为假
        sql_select = 'SELECT password FROM %s WHERE name=?' % self.table_name
        self.cur.execute(sql_select, (name,))
        return self.cur.fetchall()

    def exist_email(self, email):
        sql_select = 'SELECT password FROM %s WHERE email=?' % self.table_name
        self.cur.execute(sql_select, (email,))
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db_path = 'test_db'
    d = DataBase()
    d.insert('test', 'test', 'test')
    print(d.get_info(name='test', key_only=True))

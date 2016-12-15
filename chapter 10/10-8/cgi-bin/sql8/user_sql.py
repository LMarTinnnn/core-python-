#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from config_tel import user_table_name, user_db_path


class UserDB(object):
    def __init__(self):
        self.user_table_name = user_table_name
        self.user_db_path = user_db_path
        self.conn = sqlite3.connect(self.user_db_path)
        self.cur = self.conn.cursor()
        self.create()

    def create(self):
        sql_create = "CREATE TABLE IF NOT EXISTS %s (name TEXT, email TEXT, password TEXT)" % self.user_table_name
        self.cur.execute(sql_create)
        self.conn.commit()

    def insert(self, name, email, password):
        sql_insert = 'INSERT INTO %s VALUES(?,?,?)' % self.user_table_name
        data = (name, email, password)
        self.cur.execute(sql_insert, data)
        self.conn.commit()

    def get_info(self, name='', email='', key_only=False):
        if name:
            sql_select = 'SELECT name, password FROM %s WHERE name=?' % self.user_table_name
            self.cur.execute(sql_select, (name,))  # !!!!参数必须传tuple
            info = self.cur.fetchone()
        else:  # 用email查
            sql_select = 'SELECT name, password FROM %s WHERE email=?' % self.user_table_name
            self.cur.execute(sql_select, (email,))
            info = self.cur.fetchone()

        if info:
            key = str(info[1]) + 'salt'
            return key if key_only else (str(info[0]), key)  # !!!这里不用括号扩起来会有bug哦
        else:
            return None if key_only else (None, None)

    def exist_name(self, name):  # 存在为真 反之为假
        sql_select = 'SELECT password FROM %s WHERE name=?' % self.user_table_name
        self.cur.execute(sql_select, (name,))
        return self.cur.fetchall()

    def exist_email(self, email):
        sql_select = 'SELECT password FROM %s WHERE email=?' % self.user_table_name
        self.cur.execute(sql_select, (email,))
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    user_db_path = 'test_db'
    d = UserDB()
    d.insert('test', 'test', 'test')
    print(d.get_info(name='test', key_only=True))

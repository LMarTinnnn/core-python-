#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
db_name = 'user'
db_path = './data/user_db'


class DataBase(object):
    def __init__(self):
        self.table_name = db_name
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

    def get_data(self, number=None):
        sql_select = 'SELECT * FROM %s' % self.table_name
        self.cur.execute(sql_select)
        if number:
            return [(name, email, time) for name, email, time in self.cur.fetchmany(number)]
        else:
            return [(name, email, time) for name, email, time in self.cur.fetchall()]

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    d = DataBase()
    d.insert('test', 'test')
    d.insert('test1', 'test1')
    print(d.get_data())
    d.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
from config_tel import tel_db_path, tel_table_name


class TelDB(object):
    def __init__(self):
        self.table_name = tel_table_name
        self.db_path = tel_db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.create()

    def create(self):
        sql_create = "CREATE TABLE IF NOT EXISTS %s (name TEXT, tel TEXT, address TEXT, owner TEXT)" % self.table_name
        self.cur.execute(sql_create)
        self.conn.commit()

    def insert(self, name, email, address, owner):
        sql_insert = 'INSERT INTO %s VALUES(?,?,?,?)' % self.table_name
        data = (name, email, address, owner)
        self.cur.execute(sql_insert, data)
        self.conn.commit()

    def tel_exist(self, tel, owner):
        sql_select = 'SELECT * FROM %s WHERE tel=? and owner=?' % self.table_name
        self.cur.execute(sql_select, (tel, owner))
        if self.cur.fetchall():
            return True
        else:
            return False

    def get_data(self, number=None, owner=None):
        if owner:
            sql_select = 'SELECT name, tel, address FROM %s WHERE owner=? ORDER BY name DESC' % self.table_name
            self.cur.execute(sql_select, (owner,))
        else:
            sql_select = 'SELECT name, tel, address FROM %s ORDER BY name DESC' % self.table_name
            self.cur.execute(sql_select)

        if number:
            return [(name, tel, address) for name, tel, address in self.cur.fetchmany(number)]
        else:
            return [(name, tel, address) for name, tel, address in self.cur.fetchall()]

    def del_data(self, tel, owner):
        sql_delete = 'DELETE FROM %s WHERE tel=? AND owner=?' % self.table_name
        self.cur.execute(sql_delete, (tel, owner))
        self.conn.commit()  # 。。。不commit怎么可以啊!!!

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    tel_db_path = 'tel_test'
    d = TelDB()
    d.insert('sjdfdf', 'sdkfjdf', 'sdkf', 'test')
    # d.insert('test1', 'test1', 'test1', 'test1')
    print(d.get_data())
    print(d.get_data(owner='test'))
    d.close()

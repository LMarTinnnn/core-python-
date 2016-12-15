#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import cgi
from http.cookies import SimpleCookie
from urllib.parse import quote

import template8
from sql8 import user_sql, tel_sql
header = 'Content-Type: text/html\r\n\r\n'
url = '/cgi-bin/tel.py'
hour = 60 * 60


def valid_email(email):
    if re.match(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email):
        return True
    else:
        return False


def valid_name(name):
    if len(name) < 15:
        return True
    else:
        return False


def set_cookies(username, key):
    c = SimpleCookie()
    c['username'] = username
    c['username']['max-age'] = 4 * hour
    c['key'] = key
    c['key']['max-age'] = 4 * hour
    print(c)


def get_cookies():
    environ = os.environ
    if 'HTTP_COOKIE' in environ:
        raw_cookies = environ['HTTP_COOKIE']
        c = SimpleCookie()
        c.load(raw_cookies)
        try:
            username = c['username'].value
            key = c['key'].value
        except KeyError:
            username = key = None
    else:
        username = key = None

    return username, key


def delete_cookies():
    c = SimpleCookie()
    c['username'] = ''
    c['username']['max-age'] = 0
    c['key'] = ''
    c['key']['max-age'] = 0
    print(c)


def show_index():
    url_sign_in = url + '?action=in'
    url_sign_up = url + '?action=up'
    index_html = template8.index_temp % (url_sign_up, url_sign_in)
    print(header, index_html)


def show_error(error_str):
    error_html = template8.error_temp % error_str
    print(header, error_html)


def show_sign_up():
    up_html = template8.sign_up_temp % url
    print(header, up_html)


def show_sign_in():
    in_html = template8.sign_in_temp % url
    print(header, in_html)


def show_signed(username, db):
    db = db

    add_url = url + '?action=add'
    out_url = url + '?action=out'
    all_tel_url = '?action=all'

    data_list = db.get_data(owner=username)
    # a list like [(name, tel, address), (name2, tel2, address2)....]

    delete_link_list = [quote(url + '?action=delete&tel=%s&owner=%s' % (data[1], username)) for data in data_list]
    # quote 处理带空格的情况
    for index, (data_tuple, delete_link) in enumerate(zip(data_list, delete_link_list)):
        # ...这一点都不优雅  !! Not pythonic at all
        data_list[index] = data_tuple + (delete_link,)
    # now data_list is # a list like [(name, tel, address, link), (name2, tel2, address2,link)...]

    tr_temp = '''<tr>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td><a href="javascript:if(confirm('确实要删除吗?'))location='%s'">删除</a><td>
    </tr>'''
    tr_list = [tr_temp % data_tuple for data_tuple in data_list]
    tr_str = ''.join(tr_list)
    signed_html = template8.signed_temp % (username, add_url, tr_str, out_url, all_tel_url)
    print(header, signed_html)


def show_all_tel(db):
    data_list = db.get_data()  # a list like [(name, tel, address), (name2, tel2, address2)....]
    tr_temp = '''<tr>
          <td>%s</td>
          <td>%s</td>
          <td>%s</td>
        </tr>'''
    tr_list = [tr_temp % data_tuple for data_tuple in data_list]
    tr_str = ''.join(tr_list)
    all_tel_html = template8.all_tel_temp % tr_str
    print(header, all_tel_html)


def show_add():
    add_html = template8.form_temp % url
    print(header, add_html)


def sign_out():
    delete_cookies()
    show_index()


def delete_tel(tel, owner, db):
    db.del_data(tel, owner)


def go():
    form = cgi.FieldStorage()
    user_db = user_sql.UserDB()
    tel_db = tel_sql.TelDB()

    action = form.getvalue('action', False)
    username, key = get_cookies()  # 没有会返回两个None

    if username:   # 有cookie
        check = user_db.get_info(name=username, key_only=True)
        if key == check:
            if action == 'out':
                sign_out()
            elif action == 'all':
                show_all_tel(tel_db)
            elif action == 'add':
                show_add()

            elif action == 'delete':
                tel = form.getvalue('tel')
                owner = form.getvalue('owner')
                delete_tel(tel, owner, tel_db)
                show_signed(username, tel_db)

            elif 'add' in form:
                name = form.getvalue('name', False)
                tel = form.getvalue('tel', False)
                address = form.getvalue('address', False)
                cond1 = name and tel
                cond2 = name.strip() and tel.strip()
                if cond1 and cond2:
                    if not address or not address.strip():
                        address = '未知'
                    else:
                        address = address.strip()
                    name = name.strip()
                    tel = tel.strip()  # 不知道为何 不删除空格会有bug   QAQ ？？？
                    if not tel_db.tel_exist(tel, owner=username):
                        tel_db.insert(name, tel, address, owner=username)
                        show_signed(username, tel_db)
                    else:
                        error = '此电话已存在'
                        show_error(error)
                else:
                    error = '电话姓名不能为空'
                    show_error(error)

            else:
                show_signed(username, tel_db)
        else:
            # 验证不通过也要转index 不然下面都不会处理
            delete_cookies()
            show_index()

    else:  # 没有cookie
        if not form.keys():
            show_index()

        elif action:
            if action == 'in':
                show_sign_in()
            elif action == 'up':
                show_sign_up()

        elif 'sign_up' in form:
            if ('name' and 'email' and 'password') in form:
                username = form['name'].value
                email = form['email'].value
                password = form['password'].value
                if user_db.exist_name(username):
                    error = 'The name already exists'
                    show_error(error)
                elif user_db.exist_email(email):
                    error = 'The email already exists'
                    show_error(error)
                elif not valid_name(username):
                    error = 'Your name is too long.'
                    show_error(error)
                elif not valid_email(email):
                    error = 'The email not valid, please check its format'
                    show_error(error)
                else:
                    user_db.insert(username, email, password)
                    key = password + 'salt'
                    set_cookies(username, key)
                    show_signed(username, tel_db)
            else:
                error = 'You forget to fill in some information. Please check it'
                show_error(error)

        elif 'sign_in' in form:
            if ('email' and 'password') in form:
                email = form['email'].value
                password = form['password'].value
                username, key = user_db.get_info(email=email)
                if not key:
                    error = '账号不存在'
                    show_error(error)
                else:
                    if key == password + 'salt':
                        set_cookies(username, key)
                        show_signed(username, tel_db)
                    else:
                        error = '密码错误'
                        show_error(error)
            else:
                error = '账号或密码为空'
                show_error(error)


if __name__ == '__main__':
    go()

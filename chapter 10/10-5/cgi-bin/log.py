#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import cgi
from http.cookies import SimpleCookie

import template5
from sql import sql_helper


header = 'Content-Type: text/html\r\n\r\n'
url = '/cgi-bin/log.py'


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
    c['username']['max-age'] = 60
    c['key'] = key
    c['key']['max-age'] = 60
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
    index_html = template5.index_temp % (url_sign_up, url_sign_in)
    print(header, index_html)


def show_error(error_str):
    error_html = template5.error_temp % error_str
    print(header, error_html)


def show_sign_up():
    up_html = template5.sign_up_temp % url
    print(header, up_html)


def show_sign_in():
    in_html = template5.sign_in_temp % url
    print(header, in_html)


def show_signed(username):
    out_url = url + '?action=out'
    signed_html = template5.signed_temp % (username, out_url)
    print(header, signed_html)


def sign_out():
    delete_cookies()
    show_index()


def go():
    form = cgi.FieldStorage()
    db = sql_helper.DataBase()
    action = form.getvalue('action', False)
    username, key = get_cookies()

    if username and action != 'out':   # 有cookie 切不是登出请求的情况
        check = db.get_info(name=username, key_only=True)
        if key == check:
            show_signed(username)
        else:
            # 验证不通过也要转index 不然下面都不会执行
            delete_cookies()
            show_index()

    else:  # 没有cookie或请求登出
        if not form.keys():
            show_index()

        elif action:
            if action == 'in':
                show_sign_in()
            elif action == 'up':
                show_sign_up()
            elif action == 'out':
                sign_out()

        elif 'sign_up' in form:
            if ('name' and 'email' and 'password') in form:
                username = form['name'].value
                email = form['email'].value
                password = form['password'].value
                if db.exist_name(username):
                    error = 'The name already exists'
                    show_error(error)
                elif db.exist_email(email):
                    error = 'The email already exists'
                    show_error(error)
                elif not valid_name(username):
                    error = 'Your name is too long.'
                    show_error(error)
                elif not valid_email(email):
                    error = 'The email not valid, please check its format'
                    show_error(error)
                else:
                    db.insert(username, email, password)
                    key = password + 'salt'
                    set_cookies(username, key)
                    show_signed(username)
            else:
                error = 'You forget to fill in some information. Please check it'
                show_error(error)

        elif 'sign_in' in form:
            email = form['email'].value
            password = form['password'].value
            username, key = db.get_info(email=email)
            if not key:
                error = '账号不存在'
                show_error(error)
            else:
                if key == password + 'salt':
                    set_cookies(username, key)
                    show_signed(username)
                else:
                    error = '密码错误'
                    show_error(error)


if __name__ == '__main__':
    go()

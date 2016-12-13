#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import re

from sql_helper.sql_helper import DataBase
import template3

cgitb.enable()
header = 'Content-Type: text/html\r\n\r\n'
url = '/cgi-bin/guest_books.py'


def show_form():
    form_html = template3.form_tem % url
    print(header, form_html)


def show_error(error_str):
    error_html = template3.error_tem % error_str
    print(header, error_html)


def show_thanks(name, email):
    thanks_html = template3.thanks_tem % (name, email, url)
    print(header, thanks_html)


def show_info(data_list):
    info_template = template3.info_tem
    tr_temp = '''
    <tr>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
    </tr>'''
    tr_list = [tr_temp % (name, email, time) for name, email, time in data_list]
    info_html = info_template % ''.join(tr_list)
    print(header, info_html)


def valid_email(email):
    if re.match(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email):
        return True
    else:
        return False


def run():
    form = cgi.FieldStorage()
    db = DataBase()
    if 'info' in form:
        data_list = db.get_data()
        db.close()
        show_info(data_list)

    elif 'submit' in form:
        if 'name' not in form or form.getvalue('name').strip() == '':
            error = 'Please enter your name.'
            show_error(error)
        elif 'email' not in form:
            error = 'Please enter your email.'
            show_error(error)
        elif not valid_email(form.getvalue('email')):  # 检测合法性
            error = 'Email not valid, please check it and enter again.'
            show_error(error)
        else:
            name = form.getvalue('name')
            email = form.getvalue('email')
            # 加入数据库
            db.insert(name, email)
            show_thanks(name, email)

    else:  # 没有提交时 生成form页面
        show_form()

if __name__ == '__main__':
    run()

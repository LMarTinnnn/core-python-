#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import os

import template7
from extract_utf8 import extract_all

url = '/cgi-bin/up.py'
header = 'Content-Type: text/html\r\n\r\n'
cgitb.enable()


def show_form():
    temp = template7.form_temp
    form_html = temp % url
    print(header, form_html)


def show_result(fn, f_content):
    temp = template7.res_temp
    res_html = temp % (fn, f_content)
    print(header, res_html)


def go():
    form = cgi.FieldStorage()
    if not os.path.exists('上传文件'):
        os.mkdir('上传文件')
    os.chdir('上传文件')
    if 'upload' in form:
        up_file = form['upload']
        if up_file.file:
            fn = up_file.filename
            f_content = up_file.file.read()
            try:
                f_content = f_content.decode()
                with open(fn, 'w') as f:
                    f.write(f_content)
            except UnicodeDecodeError:
                with open(fn, 'wb') as f:
                    f.write(f_content)
                if 'zip' in fn:
                    extract_all(fn)
                    os.remove(fn)

        else:
            fn = '无效文件或空文件'
            f_content = ''

        f_content = f_content[:1024]  # 只展示前一kb内容
        if isinstance(f_content, bytes):
            f_content = '二进制内容 不做显示'

        show_result(fn, f_content)

    else:
        show_form()

if __name__ == '__main__':
    go()

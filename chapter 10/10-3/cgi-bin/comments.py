#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import template2

header = 'Content-Type: text/html\r\n\r\n'
filename = 'comments.txt'


def show_comment():
    comment_html = template2.comments_template
    print(header + comment_html)


def show_thanks():
    thanks_html = template2.thanks_template
    print(header + thanks_html)


def show_error(error_str):
    err_temp = template2.error_template
    err_html = err_temp % error_str
    print(header + err_html)


def save_comments(name, comments):
    with open(filename, 'a') as file:
        msg = '来自: %s\n评论: %s\n\n' % (name, comments)
        file.write(msg)


def run():
    form = cgi.FieldStorage()
    if 'send' in form:

        if 'name' not in form:
            error = 'Please enter your name'
            show_error(error)
        elif 'comments' not in form:
            error = 'Please input your comments'
            show_error(error)
        else:
            name = form.getvalue('name')
            comments = form.getvalue('comments')
            save_comments(name, comments)
            show_thanks()

    else:
        show_comment()

if __name__ == '__main__':
    run()

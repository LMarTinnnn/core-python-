#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cgi
import template

header = 'Content-Type: text/html\r\n\r\n'
url = '/cgi-bin/friendsC.py'
file_name = 'name_friends.txt'


def show_error(error_str):
    err_template = template.error_html
    err_html = err_template % error_str
    # !!!!!!!!! 注意是加号 这两个拼成一个字符串
    print(header + err_html)


def show_form(name, number):
    delete_url = url + '?checker=delete'
    form_template = template.form_html
    form_radio = '<input type="radio" name="number" value="%s" %s> %s'
    radio_list = []
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if str(i) == number:
            # number is a string got from the form
            # the first time user visit the show_form web_site
            # give the number param a no-string value, then no input element will be checked
            checked = 'CHECKED'
        radio_list.append(form_radio % (str(i), checked, str(i)))
    form_html = form_template % (name, url, name, ''.join(radio_list), delete_url)
    print(header + form_html)


def show_results(name, number):
    new_url = url + '?checker=reedit&name=%s&number=%s' % (name, number)
    res_template = template.res_html
    res_html = res_template % (name, name, number, new_url)
    print(header + res_html)


def show_delete():
    del_html = template.del_html
    print(header + del_html)


def add_data(filename, name, number):
    name_in = False
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if name in lines[i]:
                    lines[i] = '%s, %s\n' % (name, number)
                    name_in = True
    except IOError:
        lines = []

    if not name_in:
        lines.append('%s, %s\n' % (name, number))

    with open(file_name, 'w') as file:
        file.write(''.join(lines))


def delete_data(filename):
    try:
        with open(filename, 'w') as file:
            file.write('')
    except IOError:
        pass


def run():
    form = cgi.FieldStorage()

    if 'checker' in form:
        # 日了狗。。。。写的 'checker' == 'edit' 找了半年没看出来！！
        if form['checker'].value == 'edit':
            if 'name' not in form:
                error = 'Please enter your name.'
                show_error(error)
            elif 'number' not in form:
                error = 'Please check the number of your friends.'
                show_error(error)
            else:
                name = form['name'].value.title()
                number = form['number'].value
                add_data(file_name, name, number)
                show_results(name, number)

        elif form['checker'].value == 'reedit':
            name = form['name'].value
            number = form['number'].value
            show_form(name, number)

        elif form['checker'].value == 'delete':
            delete_data(file_name)
            show_delete()

    else:
        name = ''
        number = 0  # 非string的number不会选中input element
        show_form(name, number)

if __name__ == '__main__':
    run()

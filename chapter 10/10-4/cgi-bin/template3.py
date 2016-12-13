#!/usr/bin/env python3
# -*- coding: utf-8 -*-


form_tem = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Guest Books</title>
  </head>
  <body>
    <h1>Guest Books</h1>
    <form class="guest" action="%s" method="post">
      <p>Enter your name:  <input type="text" name="name" placeholder="Name"></p>
      <p>Enter your e-mail:
        <input type="text" name="email" placeholder="***@***.***">
      </p>
      <input type="submit" name="submit" value="Submit">
    </form>
  </body>
</html>'''

thanks_tem = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Thanks for filling</title>
  </head>
  <body>
    <h1>Thanks for filling out a guest books entry</h1>
    <p>Your name: %s</p>
    <p>Your E-mail: %s</p>
    <form action="%s" method="post">
      <input type="hidden" name="info" value="hey!">
      <p>Click <input type="submit" value="HERE"> to see all guests'info.</p>
    </form>
  </body>
</html>
'''

info_tem = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Information</title>
  </head>
  <body>
    <table border="solid">
      <tr>
        <th>姓名</th>
        <th>E-mail</th>
        <th>注册时间</th>
      </tr>
      %s
    </table>
    <form>
    <p>Click <a href="/cgi-bin/guest_books.py">HERE</a> to go back to Index</p>
  </body>
</html>'''

error_tem = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Error!</title>
  </head>
  <body>
    <h1>Error</h1>
    <p><b>%s</b></p>
    <form>
    <input type="button" value="Back" onclick="window.history.back()">
    </form>
  </body>
</html>
'''
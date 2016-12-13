#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------- html template -----------------------
error_html = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Friends CGI Demo</title>
  </head>
  <body>
      <h3>ERROR</h3>
      <p><b>%s</b></p>
      <form>
        <input type="button" name="go_back" value="Back"
        onclick="window.history.back()">
      </form>
  </body>
</html>
'''

form_html = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Friends CGI Demo</title>
  </head>
  <body>
    <h3>Friends list for: %s</h3>
    <form action="%s">
      <!-- 隐藏元素用于检测 -->
      <input type="hidden" name="checker" value="edit">
      <b>Enter your name: </b>
      <input type="text" name="name" value="%s" placeholder="User Name">
      <br />
      <b>How many friends do you have?</b>
      <!-- 用于代码生成多个表单 -->
      %s
      <br />
      <input type="submit" value="Submit">
      <p>Click <a href="%s">HERE</a> to delete all data.</p>
    </form>
  </body>
</html>
'''

res_html = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Friends CGI Demo</title>
  </head>
  <body>
    <h3>Friends list for: <i>%s</i></h3>
    <p>Your name is: <b>%s</b></p>
    <p>You have <b>%s</b> friends</p>
    <p>Click <a href="%s">HERE</a> to edit your data again</p>
  </body>
</html>
'''

del_html = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Delete Done</title>
  </head>
  <body>
    <p><h1>Have already deleted all data.</h1></p>
    <button type="button" name="button" value="Back"
    onclick="window.history.back()"></button>
  </body>
</html>
'''
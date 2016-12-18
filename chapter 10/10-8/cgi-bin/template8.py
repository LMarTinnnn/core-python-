#!/usr/bin/env python3
# -*- coding: utf-8 -*-

index_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Index</title>
  </head>
  <body>
    <h1>欢迎</h1>
    <a href="%s">注册</a>  <a href="%s">登录</a>
  </body>
</html>'''

sign_up_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>注册</title>
  </head>
  <body>
    <h1>注册</h1>
    <form action="%s" method="post">
      <p>Enter your username: <input type="text" name="name" size="25"
        placeholder="Username">  .Tips: Less than 15 characters</p>
      <p>Enter your email: <input type="text" name="email" size="25"
        placeholder="***@**.**"></p>
      <p>Enter your password: <input type="password" name="password" size="25"
        placeholder="******"></p>
      <input type="submit" name="sign_up" value="Sign Up">
    </form>
  </body>
</html>'''

sign_in_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>登录</title>
  </head>
  <body>
    <h1>登录</h1>
    <form action="%s" method="post">
      <p>Enter your email: <input type="text" name="email" size="25"
        placeholder="***@**.**"></p>
      <p>Enter your password: <input type="password" name="password" size="25"
        placeholder="******"></p>
      <input type="submit" name="sign_in" value="Sign In">
    </form>
  </body>
</html>
'''

signed_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>电话簿</title>
  </head>
  <body>
    <h1>电话簿</h1>
    <p>用户名: %s <a href="%s">添加</a></p>
    <table border="solid">
        <tr>
          <th>姓名</th>
          <th>电话</th>
          <th>住址</th>
          <th>操作</th>
        </tr>
        %s
      </table>
    <div>
      <a href=javascript:if(confirm('确实要登出吗?'))location='%s'>Sign Out</a> <a href="%s">查看全部电话簿</a>
    </div>
    <div>
        <h3>友情链接</h3>
        <a href="http://www.baidu.com/" target="_blank">百度</a>
        <a href="https://github.com/" target="_blank">GitHub</a>
        <a href="http://91.t9l.space/forumdisplay.php?fid=19&page=1" target="_blank">91Porn</a>
  </body>
</html>
'''

error_temp = '''<!DOCTYPE html>
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
    <a href='/cgi-bin/tel19.py'>回到首页</a>
  </body>
</html>
'''

all_tel_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Signed</title>
  </head>
  <body>
    <h1>电话簿</h1>
    <table border="solid">
        <tr>
          <th>姓名</th>
          <th>电话</th>
          <th>住址</th>
        </tr>
        %s
      </table>
    <div>
      <button type="button" onclick="window.history.back()">返回</button>
    </div>
  </body>
</html>
'''

form_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>添加</title>
  </head>
  <body>
    <form action="%s" method="post">
      <p>Enter name: <input type="text" name="name" placeholder="姓名"></p>
      <p>Enter tel number: <input type="text" name="tel" placeholder="电话"></p>
      <p>Enter address: <input type="text" name="address" placeholder="住址"></p>
      <input type="submit" name="add" value="Submit">
      <a href='/cgi-bin/tel19.py'>回到首页</a>
    </form>
  </body>
</html>
'''
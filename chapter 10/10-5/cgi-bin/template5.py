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
    <a href="%s">Sign Up</a>  <a href="%s">Sign In</a>
  </body>
</html>'''

sign_up_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Sign UP</title>
  </head>
  <body>
    <h1>Sign UP</h1>
    <form action="%s" method="post">
      <p>Enter your username: <input type="text" name="name" size="25"
        placeholder="Username">  Tips: Less than 15 characters</p>
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
    <title>Sign In</title>
  </head>
  <body>
    <h1>Sign In</h1>
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
    <title>Signed</title>
  </head>
  <body>
    <h1>Signed</h1>
    <p>用户名: %s</p>
    <p><a href="%s">Sign Out</a></p>
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
  </body>
</html>
'''
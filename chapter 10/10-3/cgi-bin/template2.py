#!/usr/bin/env python
# -*- coding: utf-8 -*-

comments_template = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Comments</title>
  </head>
  <body>
    <h1>Feedback</h1>
    <form class="comments" action="/cgi-bin/comments.py" method="post">
      <input type="hidden" name="send" value="yes">
      <div>
      <input type="text" name="name" placeholder="Your Name">
      </div>
      <br/ >
      <textarea name="comments" placeholder="Your comments" rows="15" cols="30"></textarea>
      <br />
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
'''

thanks_template = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Thanks</title>
  </head>
  <body>
    <h1>Thanks!</h1>
  </body>
</html>
'''

error_template = '''<!DOCTYPE html>
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
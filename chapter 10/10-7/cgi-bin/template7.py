#!/usr/bin/env python3
# -*- coding: utf-8 -*-

form_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Upload</title>
  </head>
  <body>
    <h1>Up Load</h1>
    <p><h3>Choose file to upload</h3></p>
    <form action="%s" method="post" enctype="multipart/form-data">
      <input type="file" name="upload" size="45">
      <br />
      <input type="submit" value="Submit">
    </form>
  </body>
</html>'''

res_temp = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Result</title>
  </head>
  <body>
    <h1>Upload Finished</h1>
    <p>File Name: %s</p>
    <p>Contents: <br />%s</p>
    <br />
    <button type="button" name="button"
     onclick="window.history.back()">Back</button>
  </body>
</html>
'''
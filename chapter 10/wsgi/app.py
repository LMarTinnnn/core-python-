def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    name = environ['PATH_INFO'][1:] or 'Web'
    html = '<h1>Good Morning, %s!</h1><br /><p>Sweet Heart</p>' % name
    return [html.encode()]

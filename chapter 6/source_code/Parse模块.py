from urllib import parse

if __name__ == '__main__':

    '''urlparse() 将url解析成六元组'''
    print(parse.urlparse('https://docs.python.org/3/library/index.html'))
    # ParseResult(scheme='https', \
    #             netloc='docs.python.org', path='/3/library/index.html', params='', query='', fragment='')
    print(parse.urlparse('https://docs.python.org/3/library/index.html').necloc)
    # output: 'docs.python.org'

    '''urlunparse() 将六元组(或其中一部分)重新组合成url'''
    print(parse.urlunparse(parse.urlparse('https://docs.python.org/3/library/index.html')))
    # 输出 'https://docs.python.org/3/library/index.html'

    '''urljoin(baseurl, newurl) 将baseurl的根域名拼接到newurl上'''
    base_url = 'https://docs.python.org/3/reference/index.html'
    new_url = '/library/shutil.html'
    print(parse.urljoin(base_url, new_url))
    # output: 'https://docs.python.org/library/shutil.html'
    # 有时候会在html解析出来相对域名 此时可以用urljoin()拼接


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import zipfile


def extract_all(zip_filename):
    with zipfile.ZipFile(zip_filename) as z_file:
        for name in z_file.namelist():
            utf8name = name.encode('cp437').decode()    # zipfile 内部对不能正常解码的文件用了 cp437 解码方式。。。 搞不懂
            print('解压: ', utf8name)
            dir_name = os.path.dirname(utf8name)
            data = z_file.read(name)   # 原名字读文件数据
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
            try:
                with open(utf8name, 'wb') as file:
                    file.write(data)
            except IsADirectoryError:  # namelist中会有文件夹
                pass

if __name__ == '__main__':
    extract_all('__pycache__.zip')

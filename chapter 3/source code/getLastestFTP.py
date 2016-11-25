import ftplib
import os
import socket

HOST = 'ftp.debian.org'
Path = 'pub/mozilla.org/webtools'
File = 'bugzilla-LATEST.tar.gz'


def main():
    print('start')
    ftp = ftplib.FTP(HOST)
    print('arrived')

    try:
        ftp.login()
    except:
        print('can\'t login')
    ftp.cwd(Path)
    print(ftp.pwd())
    with open(File) as file:
        ftp.retrbinary('RETR %s' % File, file.write)
    ftp.quit()


if __name__ == '__main__':
    main()

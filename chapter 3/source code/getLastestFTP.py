import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
Path = 'pub/mozilla.org/webtools'
File = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        ftp = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('can\'t reach %s' % HOST)
        print(e)
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

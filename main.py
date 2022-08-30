# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/30 23:00'


from mysql_backup import backup
from ftp_upload import upload
path = backup()
if path:
    upload(filepath=path)
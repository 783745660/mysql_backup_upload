# coding=utf-8
__author__ = 'songwenwen'
__date__ = '2022/8/30 21:34'

import os
from ftplib import FTP


def ftpconnect(host, username, password):
    ftp = FTP()
    #ftp.set_debuglevel(2)     #打开调试级别2，显示详细信息
    ftp.connect(host, 21)     #连接
    ftp.login(username, password) #登录，如果匿名登录则用空串代替即可
    return ftp


def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024        #设置缓冲块大小
    #ftp.cwd('微农贷')
    fp = open(localpath,'wb')   #以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)     #关闭调试
    fp.close()          #关闭文件


def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR '+ remotepath , fp, bufsize) #上传文件
    ftp.set_debuglevel(0)
    fp.close()
    return 0


def getFileName(filepath):
    file_list = []
    for root, dirs, files in os.walk(filepath):
        for filespath in files:
        # print(os.path.join(root, filespath))
            file_list.append(os.path.join(root, filespath))
    return file_list


def upload(filepath=""):
    host = ""
    username = ""
    password = ""
    ftp = ftpconnect(host=host, username=username, password=password)

    #########设置本地读取文件路径##############
    #filepath = 'D:\\aa\\mysql'
    file_list = getFileName(filepath)
    print(file_list)
    ftp.cwd('test')  # 进入目标服务器下的目录
    for each in file_list:
        localfile = each
        remotepath = os.path.basename(localfile)  # 要写入的文件名
        res = uploadfile(ftp, remotepath, localfile)
    ftp.quit()
    if res == 0:
        print("success")


if __name__ == "__main__":
    upload()
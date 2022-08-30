import os, time, sys


def backup():
    bakup_dir = r'D:\aa\mysql'
    current_time = time.strftime('%Y%m%d%H%M%S')
    user = ''  # 数据库用户名
    password = ''  # 数据库密码
    host = ''  # 数据库地址

    database = ["sys"]  # 指定需要备份的数据库

    if os.path.exists(bakup_dir):
        print("The path %s exists" % bakup_dir)
    else:
        # 创建文件夹
        os.makedirs(bakup_dir)
        print("The path %s create sucessful" % bakup_dir)

    # 指定当前文件夹路径
    os.chdir(bakup_dir)

    for i in range(len(database)):
        a = database[i]
        print(a)
        try:
            mysqlbak_cmd = "mysqldump -h%s -u%s -p%s --default-character-set=utf8  %s > %s%s.sql" % (
            host, user, password, a, current_time, a)
            os.system(mysqlbak_cmd)
        except Exception as e:
            print(e)
        print("backup sucessful")
    if len(os.listdir(bakup_dir)) == 0:
        print("fail")
    else:
        print("success")
        return bakup_dir
    print(1111)


if __name__ == "__main__":
    path = backup()
    print(path)
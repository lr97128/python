#! /usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = "liurui"
import telnetlib
import threading
import time

def do_telnet(tn, Host, username, password, commands):
    tn = telnetlib.Telnet(Host, port=23, timeout=10)  # 初始化一个tn实例
    tn.read_until('Username: ')
    tn.write(username + '\n')
    tn.read_until('Password: ')  # 输入密码
    tn.write(password + '\n')
    tn.read_until("#")  # 输入你要查询的命令
    for command in commands:
        flag = 1
        tn.write(command + "\n")
        while flag:
          res = tn.read_until('#', 1)
          hasit = res.find('--More--')
          if hasit > 0:
            print(res)
            tn.write(' \n')
          elif hasit == -1:
            print(res)
            break
    tn.close()


if __name__ == '__main__':
    # Host = sys.argv[1] #'172.16.100.****'
    # username=sys.argv[2]
    # password = sys.argv[3]#'9*****'
    # commands = ['show run','show interfaces']
    tn = telnetlib.Telnet('192.168.0.7', port=23, timeout=10)  # 初始化一个tn实例
    for i in range(1, 10):
        # tn = telnetlib.Telnet('192.168.0.7', port=23, timeout=10)  # 初始化一个tn实例
        t = threading.Thread(target=do_telnet, args=(tn, '192.168.0.7', 'liurui', 'Lr@824393', ['show run'],))
#    do_telnet(Host, username, password, commands)
        t.start()
        time.sleep(5)
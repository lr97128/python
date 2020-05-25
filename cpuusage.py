#!/usr/bin/env python3
# -*- coding:utf-8 -*-
_author_ = "liurui"
import telnetlib
import sys
import time

def do_showtime():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

def do_telnet(Host, username, password, command):
    tn = telnetlib.Telnet(Host, port=23, timeout=10)  # 初始化一个tn实例
    tn.read_until('Username: ')
    tn.write(username + '\n')
    tn.read_until('Password: ')  # 输入密码
    tn.write(password + '\n')
    tn.read_until("#")  # 输入你要查询的命令
    tn.write(command + "\n")
    res=tn.read_until('--More--')
    print(res)
    tn.write(' \n')
    tn.write('exit\n')
    tn.close()


if __name__ == '__main__':
    Host = "10.223.0.254"
    username = "liurui"
    password = "xxxx"
    command = "show processes cpu sorted 5sec"
    do_showtime()
    do_telnet(Host, username, password, command)

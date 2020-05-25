#! /usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = "liurui"
import telnetlib
import sys


def do_telnet(Host, username, password, commands):
    tn = telnetlib.Telnet(Host, port=23, timeout=10)  # 初始化一个tn实例
    tn.read_until('Username: ')
    tn.write(username + '\n')
    tn.read_until('Password: ')  # 输入密码
    tn.write(password + '\n')
    tn.read_until("#")  # 输入你要查询的命令
    for command in commands:
	flag=1
	tn.write(command + "\n")
	while flag:
	  res=tn.read_until('#',1)
	  hasit=res.find('--More--')
	  #print hasit
	  if hasit>0:
	    print(res)
	    tn.write('\n')
	  elif hasit==-1:
	    print(res)
  	    break
    tn.close()


if __name__ == '__main__':
    Host = sys.argv[1] #'172.16.100.****'
    print(Host)
    username=sys.argv[2]
    print(username)
    password = sys.argv[3]#'9*****'
    print(password)
    commands = ['show version']
    print(commands)
    do_telnet(Host, username, password, commands)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__="liurui"
import paramiko
import time
import threading

def reloadserver(host):
    port = 22220
    username = "liurui"
    password = "Lr@824393"
    trans = paramiko.Transport((host , port))
    trans.start_client()
    trans.auth_password(username=username,password=password)
    channel = trans.open_session()
    channel.settimeout(30)
    channel.get_pty()
    cmd = '/opt/nwreg2/local/usrbin/nrcmd\r'
    channel.invoke_shell()
    channel.send(cmd)
    time.sleep(0.3)
    rst = channel.recv(1024)
    rst = rst.decode('utf-8')
    print(rst)
    if 'username' in rst:
        cmd = 'Cnradmin\r'
        channel.send(cmd)
        time.sleep(0.3)
        rst = channel.recv(1024)
        rst = rst.decode('utf-8')
        print(rst)
    if 'password' in rst:
        cmd = 'CMTS10012\r'
        channel.send(cmd)
        time.sleep(0.3)
        rst = channel.recv(1024)
        rst = rst.decode('utf-8')
        print(rst)
    if 'nrcmd' in rst:
        cmd = 'tftp reload\r' 
        channel.send(cmd)
        time.sleep(0.3)
        rst = channel.recv(1024)
        rst = rst.decode('utf-8')
        print(rst)
    channel.close()
    trans.close()
if __name__ == '__main__':
    servers = {"10.223.40.150", "10.223.40.122", "10.223.40.134", "10.223.40.144", "10.223.40.162",
               "10.223.44.40", "10.223.44.41", "10.223.44.42", "10.223.44.43", "10.223.44.44"}
    for server in servers:
        t = threading.Thread(target=reloadserver, args=(server,))
        t.start()
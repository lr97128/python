#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import threading
_author_ = "liurui"


def reloadserver(server_ip):
    command = "/srccode/reloadtftp.sh " + server_ip
    os.system(command)

if __name__ == '__main__':
    servers = {"10.223.40.150", "10.223.40.122", "10.223.40.134", "10.223.40.144", "10.223.40.162",
               "10.223.44.40", "10.223.44.41", "10.223.44.42", "10.223.44.43", "10.223.44.44"}
    for server in servers:
        t = threading.Thread(target=reloadserver, args=(server,))
        t.start()

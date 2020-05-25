#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter as tk


top = tk.Tk()
top.title("IP计算器v1.0 作者:刘锐")
var = tk.StringVar()


def numbit(list_netmask, indx):
    num = 0
    for i in range(0, indx+1):
        if list_netmask[i] == 255:
            num += 8
        elif list_netmask[i] == 128:
            num += 1
        elif list_netmask[i] == 192:
            num += 2
        elif list_netmask[i] == 224:
            num += 3
        elif list_netmask[i] == 240:
            num += 4
        elif list_netmask[i] == 248:
            num += 5
        elif list_netmask[i] == 252:
            num += 6
        elif list_netmask[i] == 254:
            num += 7
    return num


def checkformat(ipaddr_list_str, netmask_list_str):
    if len(ipaddr_list_str) != 4 or len(netmask_list_str) != 4:
        return False
    else:
        for i in ipaddr_list_str:
            if int(i) < 0 or int(i) > 255:
                return False
                break
        for i in netmask_list_str:
            if int(i) < 0 or int(i) > 255:
                return False
                break
        return True


def subnet(ipaddr_list_str, netmask_list_str, var):
    list_netmask = []
    list_ipaddr = []
    indx = 0
    for i in netmask_list_str:
        list_netmask.append(int(i))
    for i in ipaddr_list_str:
        list_ipaddr.append(int(i))
    for i in list_netmask:
        if int(i) < 255:
            break
        indx += 1
    list_subnet = list_ipaddr.copy()
    for i in range(indx, len(list_ipaddr)):
        list_subnet[i] = (list_ipaddr[i] & list_netmask[i])
    list_broadcast = list_subnet.copy()
    for i in range(indx, len(list_ipaddr)):
        if i == indx:
            list_broadcast[i] = list_subnet[i] + (256 - list_netmask[i]) - 1
        else:
            list_broadcast[i] = 255

    num = numbit(list_netmask, indx)
    var_subnet = "网段号为:{0}.{1}.{2}.{3}\n".format(list_subnet[0], list_subnet[1], list_subnet[2], list_subnet[3])
    var_broadcast = "广播地址为:{0}.{1}.{2}.{3}\n".format(list_broadcast[0], list_broadcast[1], list_broadcast[2], list_broadcast[3])
    var_numbit = "子网位数:{0}".format(num)

    var.set(var_subnet + var_broadcast + var_numbit)


def getsubnet():
    ipaddr_str = ipaddr_entry.get().strip()
    netmask_str = netmask_entry.get().strip()
    if ipaddr_str == "" or netmask_str == "":
        var.set("IP地址或网段号不能为空！")
    else:
        ipaddr_list_str = ipaddr_str.split(".")
        netmask_list_str = netmask_str.split(".")
        result = checkformat(ipaddr_list_str, netmask_list_str)
        if result:
            subnet(ipaddr_list_str, netmask_list_str, var)
        else:
            var.set("IP地址或网段号输入格式有问题，请检查！")


top.minsize(width=400, height=200)
top.maxsize(width=400, height=200)
ipaddr_label = tk.Label(top, text="IP地址:", font='宋体 -15 bold', bg='green')
ipaddr_label.grid(row=0, column=0, rowspan=2)
ipaddr_entry = tk.Entry(top)
ipaddr_entry.grid(row=0, column=1, rowspan=2)
netmask_label = tk.Label(top, text="子网掩码:", font='宋体 -15 bold')
netmask_label.grid(row=4, column=0)
netmask_entry = tk.Entry(top)
netmask_entry.grid(row=4, column=1, rowspan=2)
display_label = tk.Label(top, textvariable=var, width=10, height=1)
commit_button = tk.Button(top, text="确定", command=getsubnet)
commit_button.grid(row=8, column=1)
display_label = tk.Label(top, textvariable=var, width=30, height=10, font='宋体 -16 bold', fg="red")
display_label.grid(row=12, column=1, rowspan=4)
# 进入消息循环
top.mainloop()





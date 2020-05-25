# list = [i for i in range(1,20) if i%3 == 0]
# print(list)
# a = 0
# b = bin(a)
# print(b)
# print(len(b))
from scapy.all import *

# mymac = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")
# # myip = IP(src=RandIP(), dst="255.255.255.255")
# # myudp = UDP(sport=68, dport=67)
# # mydhcp = DHCP(options=[("message-type", "release"), ("hostname", "MicroSoft3.0"), "end"])
# # result = sendp(mymac/myip/myudp/mydhcp)
# # print(result)
# mymac = RandMAC()
# # # print(type(mymac))
# # # print(mymac)
# # # mylist = mymac.split(":")
# # # print(mylist)
# # # print(mymac)
import time
import tkinter as tk


# def myprint():
#
#     for _ in range(0, 9):
#         print("hello world!")
#         time.sleep(3)


top = tk.Tk()
top.title("我的测试界面")
top.maxsize(400, 400)
top.minsize(400, 400)
mylabel = tk.Label(top)
mylabel.grid()

top.mainloop()
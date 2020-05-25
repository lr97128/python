#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
_author_ = "liurui"
'''
这是一个通过scapy构建arp包，进行arp攻击的程序
'''
from scapy.all import *  #导入scapy库，buneng使用import scapy.all
import os
import time
localmac = os.popen("ifconfig eth0 | grep ether | awk '{print $2}'").read()
#print localmac
broadcastmac = 'ff:ff:ff:ff:ff:ff'
macsrc = localmac
macdst = '00:00:00:00:00:00'
ipsrc = os.popen("ifconfig eth0 | grep netmask | awk '{print $2}'").read()
ifname = 'eth0'
print time.localtime(time.time())
print "  IP地址             mac地址"
for x in range(1,255):
  ipdst="10.222.0.%d" %x
  if ipdst != ipsrc:
    result = srp1(Ether(src=localmac,dst=broadcastmac)/ARP(op=1,hwsrc=macsrc,hwdst=macdst,psrc=ipsrc,pdst=ipdst),iface=ifname,timeout=0.01,verbose=False)
    if result:
      if x<10:
        print result.psrc + "        " + result.hwsrc
      elif x<100:
        print result.psrc + "       " + result.hwsrc
      else:
        print result.psrc + "      " + result.hwsrc
print time.localtime(time.time())

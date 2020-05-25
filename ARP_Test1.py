#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
_author_ = "liurui"
'''
这是一个通过scapy构建arp包，进行arp攻击的程序
'''
from scapy.all import *  #导入scapy库，buneng使用import scapy.all
import os
import threading
def maps(num,localmac,broadcastmac,macsrc,macdst,ipsrc,ifname):
  ipdst="10.222.0.%d" %num
  if ipdst != ipsrc:
    result = srp1(Ether(src=localmac,dst=broadcastmac)/ARP(op=1,hwsrc=macsrc,hwdst=macdst,psrc=ipsrc,pdst=ipdst),iface=ifname,timeout=1,verbose=False)
    if result:
      if num<10:
        print result.psrc + "        " + result.hwsrc
      elif num<100:
        print result.psrc + "       " + result.hwsrc
      else:
        print result.psrc + "      " + result.hwsrc


if __name__ == '__main__':
  print time.localtime(time.time())
  print "  IP地址             mac地址"
  localmac = os.popen("ifconfig eth0 | grep ether | awk '{print $2}'").read()
  broadcastmac = 'ff:ff:ff:ff:ff:ff'
  macsrc = localmac
  macdst = '00:00:00:00:00:00'
  ipsrc = os.popen("ifconfig eth0 | grep netmask | awk '{print $2}'").read()
  ifname = 'eth0'
  for num in range(1,255):
    t = threading.Thread(target=maps,args=(num,localmac,broadcastmac,macsrc,macdst,ipsrc,ifname,))
    t.start()
  print time.localtime(time.time())

#!/usr/bin/env python
# -*- encoding:utf-8 -*-
_author_ = "liurui"
import os
import time
import sys
import json
import threading
import MySQLdb      #连接到mysql的lib库
from DBUtils.PooledDB import PooledDB   #连接池工具lib库

def do_ping(time_out, size, host, conn):      #执行ping命令的函数
  myping = "ping -c1 -s " + size + " -W " + time_out + " " + host + " | awk -F= 'NR==2{print $4}' | awk '{print $1}'"
  result = os.popen(myping).read()     #read()函数用于将ping结果读出来 os.popen(myping)则返回的是执行结果(成功还是失败)
  if result == '\n':    #如果ping不成功，则ping的结果是回车，这个if就是判断，如果是回车，则把result修改为2
    result = '2'
  insert_db(result, conn)
  

def insert_db(result, conn):  #将ping结果插入到数据库的方法
  SQL = "insert into echoping values(" + result + ")"
  cursor = conn.cursor()
  cursor.execute(SQL)
  conn.commit()
  cursor.close()
  conn.close()



def ping_host(time_out, size, host, pool):
  while True:
    conn = pool.connection()
    t = threading.Thread(target=do_ping, args=(time_out, size, host, conn))
    t.start()
    time.sleep(1)

if __name__ == '__main__':
  time_out = 1
  size = 1500
  time_out = sys.argv[1]
  size = sys.argv[2]
  hosts = json.loads(sys.argv[3])
  pool = PooledDB(MySQLdb, 50, host='localhost', user='liurui', passwd='xxxx',db='abc',port=3306)
  for host in hosts:
    t = threading.Thread(target=ping_host, args=(time_out, size, host, pool))
    t.start()

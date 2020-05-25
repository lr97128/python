# -*- coding: UTF-8 -*-
from ldap3 import Server, Connection, ALL
import pymysql
import datetime
import threading
from DBUtils.PooledDB import PooledDB


def serchfrommysql(maccode, db):
    sql = "select maccode, cmmac1, cmmac2, remote_id, cmclass, cpeclass from cablemodems where maccode = '{0}'".format(maccode)
    cur = db.cursor()
    try:
        return cur.execute(sql)
    except Exception as e:
        raise e
    finally:
        cur.close()

def inserttomysql(entrie, mysqlconn):
    maccode = str(entrie['maccode'])
    cmmac1 = str(entrie['cmmac1'])
    cmmac2 = str(entrie['cmmac2'])
    cmclass = str(entrie['cmclass'])
    cpeclass = str(entrie['cpeclass'])
    remote_id = str(entrie['remote-id'])
    if maccode.startswith("b'5C:7D:5E:\\xb9\\xa41:D6:B8'"):
        return
    else:
        sql = "insert into cablemodems values('{0}','{1}','{2}','{3}','{4}','{5}')".format(maccode, cmmac1, cmmac2,remote_id, cmclass, cpeclass)
        cur = mysqlconn.cursor()
        try:
            cur.execute(sql)
            mysqlconn.commit()
        except Exception as e:
            mysqlconn.rollback()
            raise e
        finally:
            cur.close()
            mysqlconn.close()


def searchfromldap(ip_address, port, user, password):
    server = Server(ip_address, port=port)
    conn = Connection(server, user=user, password=password)
    # db = pymysql.connect(host='10.175.255.253', user='liurui', password='liurui97128224', db='cmplat', port=3306)
    conn.bind()
    # dn = '(&(objectclass=top)(maccode={0}))'.format(maccode)
    dn = '(&(objectclass=top))'
    conn.search('cn=mac,dc=whgd,dc=com', search_filter=dn, attributes=['maccode', 'cmmac1', 'cmmac2', 'cmclass', 'cpeclass', 'remote-id'])
    entries = conn.entries
    pool = PooledDB(creator=pymysql, mincached=10, maxcached=50, maxshared=40, maxconnections=60, blocking=True, host='10.175.255.253', user='liurui', password='liurui97128224', database='cmplat', charset="utf8")
    for entrie in entries:
        mysqlconn = pool.connection()
        t = threading.Thread(target=inserttomysql, args=(entrie, mysqlconn,))
        t.start()


if __name__ == '__main__':
    ip_address = '10.253.0.94'
    port = 1389
    user = 'cn=Directory Manager'
    password = 'onewaveinc'
    # maccode = '*'
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    searchfromldap(ip_address, port, user, password)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))





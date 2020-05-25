# -*- coding: UTF-8 -*-
from ldap3 import Server, Connection, ALL
import pymysql
import datetime



def inserttomysql(maccode, cmmac1, cmmac2, cmclass, cpeclass, remote_id):
    sql = "insert into ldap values('{0}','{1}','{2}','{3}','{4}','{5}')".format(maccode, cmmac1, cmmac2, cmclass, cpeclass, remote_id)
    db = pymysql.connect(host='10.175.255.253', user='liurui', password='liurui97128224', db='ldap', port=3306)
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
        # print("操作成功...")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cur.close()
        db.close()


def searchfromldap(ip_address, port, user, password, maccode):
    server = Server(ip_address, port=port)
    conn = Connection(server, user=user, password=password)
    conn.bind()
    dn = '(&(objectclass=top)(maccode={0}))'.format(maccode)
    conn.search('cn=mac,dc=whgd,dc=com', search_filter=dn, attributes=['maccode', 'cmmac1', 'cmmac2', 'cmclass', 'cpeclass', 'remote-id'])
    entries = conn.entries
    myfile = open("ldap.txt", "w", encoding="utf-8")
    for entrie in entries:
        maccode = entrie['maccode']
        cmmac1 = entrie['cmmac1']
        cmmac2 = entrie['cmmac2']
        cmclass = entrie['cmclass']
        cpeclass = entrie['cpeclass']
        remote_id = entrie['remote-id']
        # inserttomysql(maccode, cmmac1, cmmac2, cmclass, cpeclass, remote_id)
        myfile.write("{0}--{1}--{2}--{3}--{4}--{5}\n".format(maccode, cmmac1, cmmac2, cmclass, cpeclass, remote_id))
    myfile.close()


if __name__ == '__main__':
    ip_address = '10.253.0.94'
    port = 1389
    user = 'cn=Directory Manager'
    password = 'onewaveinc'
    maccode = '*'
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    searchfromldap(ip_address, port, user, password, maccode)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))




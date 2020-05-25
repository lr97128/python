#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__ = "liurui"
from ldap3 import Server, Connection, ALL
import datetime

# server = Server('10.253.0.94', port=1389, get_info=ALL)
server = Server('AAA-1', port=1389)
# print(server.info)
conn = Connection(server, user='cn=Directory Manager', password='onewaveinc')
# print(conn)
conn.bind()
print(conn)
# print(conn.extend.standard.who_am_i())
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# conn.search('cn=mac,dc=whgd,dc=com', '(&(objectclass=top)(cmmac2=00:01:00:01:00:01))', attributes=['maccode', 'cmclass', 'cpeclass', 'remote-id'])
# conn.search('maccode=00:01:00:01:00:01,cn=mac,dc=whgd,dc=com', '(&(objectclass=top))', attributes=['cmclass', 'cpeclass'])
# entries = conn.response_to_json()
# entries = conn.entries
# print(entries)
# for entrie in entries:
#     print(entrie["cpeclass"])
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
dn = 'MACCode=C0:50:E9:08:D2:E2,cn=mac,dc=whgd,dc=com'
# print(conn)
# conn.bind()
# conn.add(dn, ['top', 'BossMACCODE'], {'maccode': 'C0:50:E9:08:D2:E2', 'cmmac1': '1,6,C0:50:E9:08:D2:E2', 'cmmac2': 'C0:50:E9:08:D2:E2', 'cmclass': 'HRTNOTT-20M-10M-16', 'cpeclass': 'HRTN-OTT', 'remote-id': 'C0:50:E9:08:D2:E2'})
# entry = 'MACCode=C0:50:E9:08:D2:E2'
conn.delete(dn)

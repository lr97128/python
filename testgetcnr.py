#! /usr/bin/env python
# -*- coding:utf-8 -*-
_author_="liurui"
import urllib
import cookielib
data = urllib.urlencode({'name':'admin','pass':'VPN10012'})
cookie = cookielib.CookieJar()
handler = urllib.HTTPCookieProcessor(cookie)
cnrurl = 'http://10.223.40.250:9181/login.jsp'
#cnrurl = 'http://www.baidu.com'
opener = urllib.build_opener(handler)
response = opener.open(cnrurl,data,timeout=10)
#for item in cookie:
#    print 'Name = '+item.name
#    print 'Value = '+item.value
#print response.read()
clusterurl = 'http://10.223.40.250:9181/ccfg-admin/ListClusters.jsp?__vPage=cluster-list&subRoleNavBar=true'
req = urllib.Request(clusterurl)
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())

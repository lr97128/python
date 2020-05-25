#! /usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = "liurui"
import urllib
import urllib2
import cookielib
url = 'http://10.27.12.6:2003/nms/LoginSecure.jsp'
values = {'username' : 'liurui',  'password' : 'Lr@824393' }
data = urllib.urlencode(values)
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open(url,data,timeout=10)
#for item in cookie:
#    print 'Name = '+item.name
#    print 'Value = '+item.value
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#gradeUrl = 'http://10.27.12.6:2003/nms/Common/Inc/NodeMenu.jsp?ENABLEALL=yes&AuthMode=VIEW&JSType=null'
#gradeUrl = 'http://10.27.12.6:2003/nos/failure/malfunctionmanage/AlarmInfoList.jsp?flag=RealAlarmBoard&IFTTRAP=N&AlarmLevelList=5%2C4%2C3%2C2%2C1&sUIID=RealAlarmBoard&MenuNodeName=%CE%E4%BA%BA&MenuNodeCode=NOD999&QueryFlag=null&AuthMode=VIEW&AlarmClass=&ResClass=&ResName=&Summary=&AlarmLevels=5&AlarmLevels=4&AlarmLevels=3&AlarmLevels=2&AlarmLevels=1'
gradeUrl = 'http://10.27.12.6:2003/nos/failure/Common/Scripts/ResAlarmInfo.js'
result = opener.open(gradeUrl)
print result.read()

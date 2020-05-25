#! /usr/bin/env python3
# -*- coding:utf-8 -*-
_author_ = "liurui"
import urllib.request
import json
if __name__ == '__main__':
#微信公众号上应用的CropID和Secret
    CropID='xxxx'
    Secret='xxxxxx'
#获取access_token
    GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" %(CropID,Secret)
#    result=urllib.request.urlopen(urllib.request.Request(GURL)).read()
    result=urllib.request.urlopen(GURL).read()
    dict_result = json.loads(result)
    Gtoken=dict_result['access_token']
    print(Gtoken)
#生成通过post请求发送消息的url
    PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" %Gtoken
#企业号中的应用id
    AppID=1000002
#部门成员id，微信接收者
    UserID='001'
#部门id，定义可接收消息的成员范围
    PartyID=1
#生成post请求信息
    post_data = {}
    msg_content = {}
    msg_content['content'] = "123"
    post_data['touser'] = UserID
    post_data['toparty'] = PartyID
    post_data['msgtype'] = 'text'
    post_data['agentid'] = AppID
    post_data['text'] = msg_content
    post_data['safe'] = '0'
    print(post_data)
    print(json.dumps(post_data))
#python3的urllib合并了python2的urllib与urllib2的功能，并且python3的urllib的各个open方法都对data进行了要求，
#只能使用byte类型不能用str类型，而bytes方法又不能直接对字典类型进行转换，只能将字典通过json的dumps方法转换
#为json格式的str，然后再使用bytes方法对json格式进行转换，转换为byte类型
    json_post_data=(bytes(json.dumps(post_data), 'utf-8'))
    req = urllib.request.urlopen(url=PURL, data=json_post_data)
    print(req.read())
#    opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
#    request_post = opener.open(req).read()
#    print(request_post)


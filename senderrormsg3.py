#! /usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__="liurui"
import urllib.request
import json

def gettoken() -> str:
	'''
	获取企业微信的令牌
	:return: 返回企业微信返回的令牌信息。
	'''
	CropID='wwd95f383ca206fe22' #企业微信为公司生成的组织ID
	Secret='29xZnVramS2ZsAf38iXGa8X1YxVFBGtiGh_X7UTGl-s' #企业微信为公司生成的密钥
	GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" %(CropID,Secret)
	result=urllib.request.urlopen(GURL).read()
	json_result=json.loads(result)
	token=json_result['access_token']
	return token

def send_msg(token, post_data) -> str:
	'''
	通过企业微信发送告警信息到企业负责人。
	:param token: 企业微信需要的令牌
	:param post_data: 是个字典类型的数据，是根据企业微信接口需要的信息
	:return: 返回一个企业微信返回的信息。
	'''
	PURL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" %token
	json_data = json.dumps(post_data, skipkeys=False, ensure_ascii=False) #ensure_ascii的值必须为False，否则中文会是乱码发送到手机客户端
	json_result = urllib.request.urlopen(url=PURL, data=(bytes(json_data, 'utf-8'))).read()
	result = json.loads(json_result)['errmsg']
	return result

if __name__ == "__main__":
	myToken =gettoken()
	post_data = {}
	msg_content = {}
	AppID = 1000002
	UserID = '001'
	PartyID = 1
	msg_content['content'] = "你好！"
	post_data['touser'] = UserID
	post_data['toparty'] = PartyID
	post_data['msgtype'] = 'text'
	post_data['agentid'] = AppID
	post_data['text'] = msg_content
	post_data['safe'] = '0'
	result = send_msg(myToken, post_data)
	print(result)

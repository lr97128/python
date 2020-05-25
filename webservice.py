#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__ = "liurui"
#from suds.client import Client
import urllib

wsdl_url = 'http://10.253.0.101:10024/services/AAAServer'


def creat_maccode(maccode):
    authenticationRequest = """
    <?xml version="1.0" encoding="gb2312"?>
    <wsdl:definitions targetNamespace="http://aaa.ws.boss.huashu.com" xmlns:apachesoap="http://xml.apache.org/xml-soap" xmlns:impl="http://aaa.ws.boss.huashu.com" xmlns:intf="http://aaa.ws.boss.huashu.com" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:wsdlsoap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
       <wsdl:message name="authenticationRequest">
       <wsdl:part name="in0" type="xsd:string"/>
   </wsdl:message>
    <Root>
    <Action code="MACADD" seqno="" spcode="bd1">
    <info type="mac">
    <property name="maccode" value="{0}"/>
    <property name="remote-id" value="{0}"/>
    <property name="cmclass" value="HRTN-20M-10M-16"/>
    <property name="cpeclass" value="HRTN"/>
    <property name="cmmac1" value="1,6,{0}"/>
    <property name="cmmac2" value="{0}"/>
    </info>
    </Action>
    </Root>
    """.format(maccode)
    # print(authenticationRequest)
    # client = Client(wsdl_url)
    # print(client)
    # client.service.authentication(authenticationRequest)
    # req = str(client.last_sent())
    # response = str(client.last_received())
    # print(req)
    # print(response)
    req = urllib.request.Request(wsdl_url, data=authenticationRequest.encode('gb2312'), headers={'Content-Type': 'text/xml'})
    urllib.request.urlopen(req)


if __name__ == '__main__':
    maccode = "ff:ff:ff:ff:ff:fe"
    creat_maccode(maccode)


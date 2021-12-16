#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
_author_ = "liurui"
from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import sys

#此句用于消除ssl证书错误，exchange使用自签证书需要加上
#BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

def sendMail(account, cost):
  fd = open('/root/sendMail/admin', mode='r')
  result = fd.readline()
  if result == 'Yes':
    print('已经发过邮件了')
    fd.close()
  else:
    msg = '''你好可天，

账号     xxxx  费用不足(目前费用为: {})；  请帮忙充值5000000  ， 此账号用于inpaas、大数据、ELK、安全屋  等产品项目产品线业务 生产环境使用
<br><br>

请xxx帮忙确认  @韩旭光
<br><br>
谢谢
    '''.format(cost)
    m = Message(
      account=account,
      subject='产品线账号充值',
      body=HTMLBody(msg),
      to_recipients=['收件人1','收件人2'],
      cc_recipients=['cc邮箱地址1', 'cc邮箱地址2']
    )
    m.send_and_save()
    print('admin账号充值邮件发送完毕')
    fd = open('/root/sendMail/admin', mode='w')
    fd.write('Yes')
    fd.close()

#输入你的域账号
def app(user, passwd):
  credentials = Credentials(username=user, password=passwd)
  account = Account('收件邮箱地址', credentials=credentials, autodiscover=True)
  adminValueNew = 0
  adminValueOld = 0
  print('连接邮箱成功')
  #for item in account.inbox.all().order_by('-datetime_received')[:40]:
  #  print(item.sender)
  for item in account.inbox.glob('cost').all().order_by('-datetime_received')[:1]:
    for model in item.text_body.split('\n'):
      if '关键字' in model:
        model.strip(' ')
        adminValueNew = int(model.split(' ')[34].split('.')[0])
  if adminValueNew > 5000000:
    fd = open('/root/sendMail/admin', mode='w')
    fd.write('No')
    fd.close()
    print("已经有500万了...")
    return
  for item in account.inbox.glob('cost').all().order_by('-datetime_received')[1:2]:
    for model in item.text_body.split('\n'):
      if '关键字' in model:
        model.strip(' ')
        adminValueOld = int(model.split(' ')[34].split('.')[0])
  adminCostPerDay = adminValueOld - adminValueNew
  if adminValueNew <= adminCostPerDay * 7:
    sendMail(account, adminValueNew)
  else:
    print("admin账号余额够7天使用，不需要发邮件")

if __name__ == "__main__":
  passwd = sys.argv[1]
  app('cds\\rui.liu', passwd)

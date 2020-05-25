#!/usr/bin/env python
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.223.40.150", 22, "root", "WhcatvManage@2014")
stdin, stdout, stderr = ssh.exec_command("uname")
print(stdout.readlines())
#std = ssh.connect("10.33.33.46",22220,"liurui", "Lr@824393")
#print std
ssh.close()

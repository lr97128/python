ipaddr = "192.168.31.254"
netmask = "255.255.128.0"
list_netmask = []
list_ipaddr = []
list_broadcast = []
list_str_netmask = netmask.split('.')
list_str_ipaddr = ipaddr.split('.')
for i in list_str_netmask:
    list_netmask.append(int(i))
for i in list_str_ipaddr:
    list_ipaddr.append(int(i))
indx = 0
for i in list_netmask:
    if int(i) < 255:
        break
    indx += 1
list_subnet = list_ipaddr.copy()
for i in range(indx,len(list_ipaddr)):
    list_subnet[i] = (list_ipaddr[i] & list_netmask[i])
list_broadcast = list_subnet.copy()
for i in range(indx,len(list_ipaddr)):
    if i == indx:
        list_broadcast[i] = list_subnet[i] + (256 - list_netmask[i]) - 1
    else:
        list_broadcast[i] = 255
print("网段号为:{0}.{1}.{2}.{3}".format(list_subnet[0],list_subnet[1],list_subnet[2],list_subnet[3]))
print("广播地址为:{0}.{1}.{2}.{3}".format(list_broadcast[0],list_broadcast[1],list_broadcast[2],list_broadcast[3]))
#!/usr/bin/env python2.7
n = 25
myList = []
onDesk = []
for i in range(1, (n+1)):
    myList.append(i)
print(myList)
count = len(myList)
i = 3
while count > 0:
    i += 1
    if count == 1:
        num = myList[0]
        myList.remove(num)
        onDesk.append(num)
        break
    elif i % 2 == 0:
        num = myList[0]
        myList.remove(num)
        myList.append(num)
    else:
        num = myList[0]
        myList.remove(num)
        onDesk.append(num)
    count = len(myList)
print(onDesk)


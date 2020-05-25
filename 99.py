#!/usr/bin/env python3
for i in range(1,10):
	for j in range(1,i+1):
        #print函数打印完毕后会自动换行
		print("%-2d * %-2d = %-4d" %(i,j,i*j), end=" ")
	print("\n")
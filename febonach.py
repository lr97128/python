#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__="liurui"

def fid(n) -> list:
	'''
	产生斐波那契数列
	:param n:表示第N个数字
	:return:返回list，该list是斐波那契数列
	'''
	l = []
	if n >= 1:
		l.append(1)
	if n >= 2:
		l.append(1)
	if n > 2:
		x = 1
		y = 1
		for _ in range(3,n+1):
			temp = x
			x = x + y
			y = temp
			l.append(x)
		return l
if __name__ == '__main__':
	num = fid(12)
	print(num)

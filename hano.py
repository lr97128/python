#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__ = "liurui"
'''
1、问题一：每次自调用的时候，中间状态的起始塔、目标塔、中间塔是变化的，因此不能通过打印a、b、c来反应现实中一直不变的起始塔、中间塔、目标塔
2、问题二：通过定义一个现实中的塔：src--起始塔、dst--目标塔、mid--中间塔，并且把第一次调用函数时的传参，第一次调用时main函数调用，已经很明确了最终的起始塔为a、
目标塔为dst、中间塔为mid。但是同样出现另一个问题，函数自调用的时候，也会重新将src、dst、mid重新赋值为中间状态的a、b、c，而这时候的a、b、c并不是现实中最终的起始塔、
目标塔、中间塔。因此定义了一个关键字参数flag，main函数调用hano函数时，由于没有对flag进行传参，因此flag是缺省的True，这样，才会对src、dst、mid进行赋值，
而中间函数自调用的时候，flag赋值为False，这样，将不会对src、dst、mid进行重新赋值
3、如此，才能保证src代表着现实中始终不变的起始塔a、dst代表着现实中始终不变的目标塔b、mid代表着现实中始终不变的中间塔c
'''

def printall(a, b, c) -> None :
    print(a, end=" ")
    print(b, end=" ")
    print(c)


def hano(n, a, b, c, flag=True):
    global src
    global dst
    global mid
    if flag:
        src = a
        dst = b
        mid = c
    if n == 1:
        num = a[0]
        b.insert(0, num)
        a.remove(num)
        printall(src, dst, mid)
        return None
    if n > 1:
        hano(n-1, a, c, b, flag=False)
        num = a[0]
        b.insert(0, num)
        a.remove(num)
        printall(src, dst, mid)
        hano(n-1, c, b, a, flag=False)

if __name__ == '__main__':
    n = 5
    a = []
    b = []
    c = []
    for i in range(1, n+1):
        a.append(i)
    printall(a, b, c)
    hano(n, a, b, c)
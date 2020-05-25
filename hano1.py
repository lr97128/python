#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__auther__ = "liurui"


def print_All(a, b, c):
    print(a, end=" ")
    print(b, end=" ")
    print(c)


def hano(n, a, b, c, flag=False):
    global src
    global dst
    global midd
    if flag:
        src = a
        dst = b
        midd = c
    if n == 1:
        num = a[0]
        b.insert(0, num)
        a.remove(num)
        print_All(src, dst, midd)
        return None
    hano(n-1, a, c, b)
    num = a[0]
    b.insert(0, num)
    a.remove(num)
    print_All(src, dst, midd)
    hano(n-1, c, b, a)


if __name__ == '__main__':
    n = 4
    a = []
    b = []
    c = []
    for i in range(1, n+1):
        a.append(i)
    print_All(a, b, c)
    hano(n, a, b, c,flag=True)
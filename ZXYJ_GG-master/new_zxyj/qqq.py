#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3/003 17:44
# @Author  : 刘登攀
# @Site    : 
# @File    : qqq.py
# @Software: PyCharm
a = '2020-01-04 00:00:00'
if '2020-01-01 00:00:00' <= a <= '2020-01-02 23:59:59':  # 判断订单支付时间
    print('1')
else:
    print('2')
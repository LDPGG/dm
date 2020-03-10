#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29/029 21:01
# @Author  : 刘登攀
# @Site    : 
# @File    : hhh.py
# @Software: PyCharm
import requests


path = r'C:\Users\Administrator\Desktop\ttt.txt'
# 读取记事本内容
phones = open(path, 'r').readlines()

i = 3
for a in phones:
    phone = a.strip()

    session = requests.Session()

    #
    url = 'http://g.zxyj.com/flyweb/numerousMeet/addBaseTag'
    url_post = {'type': '0',
                'sortIndex': '%s' % i,
                'name': '%s' % phone
                }
    session.post(url, url_post)
    print(i)
    i = i + 1




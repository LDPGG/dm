#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24/024 20:05
# @Author  : 刘登攀
# @Site    : 
# @File    : add.py
# @Software: PyCharm
import requests



session = requests.session()

url = 'http://39.108.195.48:8080/groupWebApi/login?version=1.0&terminal=3'
data = {'username': 'yyg', 'password': '123456'}
session.post(url, data)

sp_url = 'http://39.108.195.48:8080/groupApi/product/add'
sp_data = {'version': '1.0',
           'storeId': '1545dajksdas',
           # 一级id
           'parentClassifyId': '4b9767885bb04f799ed6d23e2581627b',
           # 二级id
           'classifyId': '78469ebe8e8f4730be8d66ceae9b573e',
           # 品牌id
           'brandId': '6a5859536d134b4dbea2d46977d76601',
           'productName': '六六六',
           'status': '1',
           'isShippingFree': '1',
           'itemCode': '123',
           'unship': '0',
           'isLimit': '0',
           'content': '1234654',
           'parentSpecId': '1598a6f03d14c4739aff2d2b92b2b13ec',
           'parentSpecId2': 'd8b61de05c0f42979bb93452d7a13468',
           'freightId': '2',
           'type': '1',
           'freeQuantity': '0'
           }
a = session.put(url=sp_url, data=sp_data).json()
print(a)






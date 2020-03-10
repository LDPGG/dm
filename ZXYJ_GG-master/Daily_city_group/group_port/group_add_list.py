#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23/023 11:21
# @Author  : 刘登攀
# @Site    : 
# @File    : group_add_list.py
# @Software: PyCharm
import requests
import threading


def add_list():
    session = requests.session()
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': '13266590422',
                   'password': '123456'}
    session.post(ht_log_url, ht_log_data)

    menuName = ['产品erp同步', '订单erp同步']
    menuUrl = ['/productErp', '/orderErp']

    for i in range(len(menuUrl)):
        # print(menuName[i], menuUrl[i])

        add_list_url = 'http://39.108.195.82:8080/groupWebApi/menu/add?' \
                       'parentMenuId=146&menuName=%s&menuUrl=%s&status=1&menuSort=99&type=2&version=1.0' % (menuName[i], menuUrl[i])
        a = session.put(add_list_url).json()
        print(menuName[i], a['message'])






threading.Thread(target=add_list(600))

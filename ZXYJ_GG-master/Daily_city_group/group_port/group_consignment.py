#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14/014 15:10
# @Author  : 刘登攀
# @Site    : 
# @File    : group_consignment.py
# @Software: PyCharm
import requests
import threading

session = requests.Session()


# 后台确认收货
def consignment(conten):
    i = 1
    while i <= conten:
        ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
        ht_log_data = {'username': 'ldp001',
                       'password': '123456'}
        session.post(ht_log_url, ht_log_data)

        url = 'http://39.108.195.82:8080/groupWebApi/order/list/pager?pageOffset=1&pageSize=10&status=2&version=1.0'
        order = session.get(url).json()
        order_code_1 = order['data']['datas'][0]['orderCode']

        ht_fh_url = 'http://39.108.195.82:8080/groupWebApi/order/ship?expressName=&expressCode=11111&expressNo=JD&orderCode=%s&version=1.0' % order_code_1
        a = session.post(ht_fh_url).json()
        print(order_code_1, a['message'], i)

        login_url = 'http://39.108.195.100:8088/groupApi/wechatLogin'
        # # ogLGp5Z8THB-t1rPk53QRc-i1Qn0
        # ogLGp5UiGQ70tEqpuSqwUhEWB2hM
        login_date = {'openId': 'ogLGp5UiGQ70tEqpuSqwUhEWB2hM',
                      'version': '1.0'}
        session.post(login_url, login_date).json()

        # a_url = 'http://39.108.195.100:8088/groupApi/order/list/search?status=3&keyword=&pageOffset=1&pageSize=10&version=1.0&terminal=4'
        # a = session.get(a_url).json()
        # order_code_1 = a['data']['datas'][0]['orderMain']['orderCode']

        sh_url = 'http://39.108.195.100:8088/groupApi/order/received'
        sh_data = {'orderCode': order_code_1,
                   'version': '1.0'}
        b = session.post(sh_url, sh_data).json()
        print(order_code_1, b['message'])
        i += 1


threading.Thread(target=consignment(2))


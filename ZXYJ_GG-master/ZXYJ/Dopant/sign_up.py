#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19/019 14:24
# @Author  : 刘登攀
# @Site    : 
# @File    : sign_up.py
# @Software: PyCharm
import requests
from random import Random


def sign():

    session = requests.session()
    # 随机生成token
    length_r = 32
    token = ''
    chars = '01'
    length = len(chars) - 1
    random = Random()
    for i in range(length_r):
        token += chars[random.randint(0, length)]

    url = 'http://39.108.195.48:8080/flyapi/apply/add'
    date = {'token': token,
            'version': '1.0',
            'applyName': '徐鹏鹏测试1',
            'phone': '18612483431',
            'email': '',
            'wechat': '',
            'tram': '1'}
    a = session.post(url=url, data=date).json()
    print(a)


if __name__ == '__main__':
    sign()

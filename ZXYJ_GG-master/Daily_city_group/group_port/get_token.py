#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14/014 20:35
# @Author  : 刘登攀
# @Site    : 
# @File    : get_token.py
# @Software: PyCharm
from random import Random


# 随机生成token
def get_token():
    length_r = 32
    token = ''
    chars = '01'
    length = len(chars) - 1
    random = Random()
    for i in range(length_r):
        token += chars[random.randint(0, length)]
    return token


if __name__ == '__main__':
    for i in range(5200):
        print(get_token())

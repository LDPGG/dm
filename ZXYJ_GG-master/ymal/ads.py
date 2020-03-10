#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10/010 16:46
# @Author  : 刘登攀
# @Site    : 
# @File    : ads.py
# @Software: PyCharm

import yaml
import os
import requests

# 获取当前脚本所在文件路径
cutPath = os.path.dirname(os.path.realpath(__file__))
# 获取ymal文件路径
yamlpath = os.path.join(cutPath, "ttt.yaml")

# open方法打开读取
f = open(yamlpath, 'r', encoding='utf-8')
d = yaml.load(f)

print(d)
# session = requests.Session()
# url_login_test = "http://39.108.195.48:8080/flyweb/user/login"
# login = session.post(url_login_test, data=d[1])  # 用post请求获得session
# print(login)

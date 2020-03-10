#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23/023 14:27
# @Author  : 刘登攀
# @Site    : 
# @File    : zxyj_refund.py
# @Software: PyCharm
import requests


def refund():
    session = requests.session()
    url_login_test = "http://39.108.195.48:8080/flyweb/user/login"
    test_login_data = {'username': 'admin', "passwd": 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(url_login_test, data=test_login_data)

    buy_refund_url = ''

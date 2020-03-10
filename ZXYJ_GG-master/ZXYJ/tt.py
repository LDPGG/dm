#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4/004 11:28
# @Author  : 刘登攀
# @Site    : 
# @File    : get_token.py
# @Software: PyChar
import requests
import json

session = requests.session()
headers = {'content-type': "application/json"}
b = 'https://passport.qyer.com/qcross/passport/register/mobile/checkmobile?ajaxID=591d04b6733e86c93db2a1b0'
c = {'mobile': '8615386174586'}
a = requests.post(b, data=json.dumps(b), headers=headers).json()
print(a)
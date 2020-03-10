#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16/016 10:57
# @Author  : 刘登攀
# @Site    : 
# @File    : ttttttt.py
# @Software: PyCharm
import requests


def sign_in(phone, wechatOpenId, invitationCode):
    headers = {'ContentType': "application/json"}
    url = 'http://39.108.195.100:8088/groupApi/user/add?phone=%s&password=e10adc3949ba59abbe56e057f20f883e&nickName=thename&userName=name&identityCard=86288802542027846&' \
          'wechatOpenId=%s&wechat=bin_luyck&wechatUnionId=100SDASAD03ASDSA1587&invitationCode=%s&version=1.0' % (phone, wechatOpenId, invitationCode)
    add_user = requests.put(url, headers=headers).json()
    print(add_user)

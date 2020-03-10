#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7/007 17:20
# @Author  : 刘登攀
# @Site    : 
# @File    : zhuce.py
# @Software: PyCharm
import requests
import json
from bs4 import BeautifulSoup
import re
'''
阿胖：批量注册用户
'''

def zhuce():
    session = requests.Session()
    # # # 接口上传图片
    headers = {"ct": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}
    # toux = 'http://47.105.132.102:8080/xyapi/upload/img'
    # files = {'file': ('tt.jpg', open(r'C:\Users\Administrator\Desktop\tt.jpg', 'rb'), 'image/jpeg')}
    # tox_post = {'version': '1.0'}
    #
    # ppp = session.post(toux, tox_post, files=files, headers=headers)
    # print(ppp.json())
    #
    # 读取用户信息
    with open(r'C:\Users\Administrator\Desktop\虚拟数据.txt', 'r', encoding='utf-8') as f:
        res = f.read()
    # 读取昵称
    with open(r'C:\Users\Administrator\Desktop\nicheng.txt', 'r', encoding='utf-8') as f:
        nic = f.read()
    with open(r'E:\dm\djongo\dy.txt', 'r', encoding='utf-8') as f:
        dy = f.read()

    # 遍历文档
    # 用户数据
    yh_soup = BeautifulSoup(res, "html.parser")
    # 昵称
    nc_soup = BeautifulSoup(nic, "html.parser")
    # 视频内容
    dy_soup = BeautifulSoup(dy, "html.parser")
    address = re.findall('(.*?)\n', '%s' % dy_soup)

    phone = re.findall('tel=(.*?),', '%s' % yh_soup)
    nc = re.findall('(.*?)\n', '%s' % nc_soup)
    name = re.findall('name=(.*?),', '%s' % yh_soup)

    for i in range(len(nc)):
        # 注册
        # nc[i] = nc[i].replace('\r', '').replace('\n', '').replace('\xa0', '').replace('\t', '')
        # t_url = 'http://47.105.132.102:8080/xyapi/user/add?version=1.0&phone=%s' \
        #         '&password=e10adc3949ba59abbe56e057f20f883e&nickName=%s' \
        #         '&userName=%s&headImage' % (phone[i], nc[i], name[i])
        # a = session.put(t_url)
        # print(a.json())

        # 登录
        login_url = 'http://47.105.132.102:8080/xyapi/login'
        login_post = {'version': '1.0',
                      'username': phone[i],
                      'password': 'e10adc3949ba59abbe56e057f20f883e'}
        login = session.post(login_url, data=login_post).json()
        print(login['message'])
        # # for video in range(1, 101):

        # 上传视频
        upload_url = 'http://47.105.132.102:8080/xyapi/upload/video'
        upload_post = {'version': '1.0'}
        i = i + 1
        files_01 = {'file': ('%s.mp4' % i, open(r'E:\视频\抖音\%s.mp4' % i, 'rb'), 'image/jpeg')}

        upload = requests.post(upload_url, data=upload_post, files=files_01, headers=headers).json()
        video_url = upload['data']['url']

        # 发布视频
        release_url = 'http://47.105.132.102:8080/xyapi/circle/add/release'
        release_post = {'version': '1.0',
                        'content': '%s' % address[i],
                        'type': '3',
                        'video': video_url
                        }
        release = session.post(release_url, data=release_post).json()
        print(release)




if __name__ == '__main__':
    zhuce()

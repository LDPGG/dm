#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15/015 15:42
# @Author  : 刘登攀
# @Site    : 
# @File    : nzw.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re


def nzw():
    url = 'http://tieba.baidu.com/p/3108805355?pn=1'
    html = requests.get(url=url)
    soup = BeautifulSoup(html.text, 'html.parser')
    fall = soup.find_all(class_='d_post_content_main')
    url = re.findall('pic_type="0" src="(.*?)\.jpg"', '%s' % fall)
    for i in range(len(url)):
        print('%s.jpg' % url[i])


if __name__ == '__main__':
    nzw()

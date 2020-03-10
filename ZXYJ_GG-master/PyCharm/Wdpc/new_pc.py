#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15/015 10:14
# @Author  : 刘登攀
# @Site    : 
# @File    : new_pc.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
import re


def pc():
    url = 'https://www.qiushibaike.com/pic/'
    we_data = requests.get(url)
    soup = BeautifulSoup(we_data.text, 'html.parser')
    image_url = soup.find_all(class_='article block untagged mb15')
    image = re.findall('<span>(.*?)</span>', '%s' % image_url)
    url = re.findall(r'src="(.*?)\.jpg"', '%s' % image_url)
    for i in range(len(image)):
        a = image[i].replace('<br/>', '')
        print('内容：%s\n图片地址：https:%s' % (a, url[i]))
        print('\t')


if __name__ == '__main__':
    pc()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17/017 14:20
# @Author  : 刘登攀
# @Site    : 
# @File    : reconsitution.py
# @Software: PyCharm
from selenium import webdriver
import re

'''
根据作者爬取视频
'''


class Recons(object):
    def __init__(self):
        url = 'https://kuaiyinshi.com/hot/author/?source=kuai-shou&page=1'
        self.driver = webdriver.PhantomJS(executable_path='E:\Python36\Lib\site-packages\phantomjs-2.1.1-windows\\bin\phantomjs.exe')
        self.driver.get(url)
        self.page = self.driver.page_source
        # https://kuaiyinshi.com
        a = re.findall('class="avatar" href="(.*?)"', '%s' % self.page)
        for i in range(len(a)):
            b = 'https://kuaiyinshi.com%s' % a[i].replace('amp;', '')
            self.driver.get(b)
            self.page = self.driver.page_source
            title = re.findall('list-item-desc">(.*?)</p>', '%s' % self.page)
            c = re.findall('href="(.*?)&amp;source=', '%s' % self.page)
            for ii in range(len(title)):
                d = 'https://kuaiyinshi.com%s&source=huo-shan#search-form' % c[ii]
                self.driver.get(d)
                self.page = self.driver.page_source
                e = re.findall('src="(.*?)" type', '%s' % self.page)
                title = re.findall('class="desc">(.*?)</p>', '%s' % self.page)
                for iii in range(len(e)):
                    print('视频内容:%s\n视频链接:https:%s' % (title[i], e[i]))


if __name__ == '__main__':
    Recons()

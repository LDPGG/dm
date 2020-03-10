#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17/017 13:38
# @Author  : 刘刘刘刘大爷
# @Site    : 
# @File    : test_ttt.py
# @Software: PyCharm
from selenium import webdriver
url = "-----假装是个url-------------"
# executable_path后面填你写进path环境的路径 ----刘刘刘刘大爷
driver = webdriver.PhantomJS(executable_path='E:\Python36\Lib\site-packages\phantomjs-2.1.1-windows\\bin\phantomjs.exe')
driver.get(url)
print(driver.page_source)
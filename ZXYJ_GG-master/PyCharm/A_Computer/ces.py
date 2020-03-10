#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29/029 16:19
# @Author  : 刘登攀
# @Site    : 
# @File    : ces.py
# @Software: PyCharm
from selenium import webdriver
import time
import os
os.system(r'C:\Users\Administrator\Desktop\tttttt.exe')
import win32gui

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://39.108.195.48:8080/flyweb/user/login")
driver.implicitly_wait(20)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("passwd").clear()
driver.find_element_by_id("passwd").send_keys("123456")
driver.find_element_by_id("submit_login").click()

driver.find_element_by_link_text(u"产品管理").click()

driver.find_element_by_link_text(u"产品列表").click()
time.sleep(1)
driver.switch_to.frame('mainFrame')
driver.find_element_by_xpath('/html/body/div/input[2]').click()
time.sleep(2)
# driver.find_element_by_id('file-1').click()
driver.find_element_by_xpath('//*[@id="videoBox"]/div/div/div[4]/div[2]/div').click()
os.system(r'C:\Users\Administrator\Desktop\tttttt.exe')

time.sleep(20)
driver.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 15:15
# @Author  : duanww
# @File    : automationWe_demo.py
# @Software: PyCharm


from appium import webdriver
import time
import warnings
import time
import unittest


desired_caps = {'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '3389c0c4',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
                }

warnings.simplefilter("ignore", ResourceWarning)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id('com.tencent.mm:id/iq').click()
time.sleep(1)
driver.find_element_by_id('com.tencent.mm:id/kh').send_keys('css')
time.sleep(3)
driver.find_element_by_id('com.tencent.mm:id/q0').click()
# driver.find_element_by_id('com.tencent.mm:id/bpg').click()
time.sleep(3)
# print(driver.contexts)
print(driver.contexts[1])
# 有的手机打印没有web这个，（注：7.0.3版本的微信打印直接报错的）（appium的软件在手机端点安装就可以解决了）（每次重新打开appium，app端的软件就要重新安装）
# ['NATIVE_APP', 'WEBVIEW_com.tencent.mm:tools']
driver.switch_to.context(driver.contexts[1])
#
driver.find_element_by_xpath('//*[@id="main-tab-top"]/div[4]/div[2]').click()
print('成功跳转【我】页面\n')
time.sleep(1)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7/007 17:01
# @Author  : 刘登攀
# @Site    : 
# @File    : up.py
# @Software: PyCharm
from appium import webdriver
import warnings
import time
print(1==2)
#
# def up():
#     warnings.simplefilter("ignore", ResourceWarning)
#     desired_caps = {'platformName': 'Android',
#                     'platformVersion': '5.1.1',
#                     'deviceName': '3389c0c4',
#                     'appPackage': 'com.tencent.mm',
#                     'appActivity': '.ui.LauncherUI',
#                     'automationName': 'Uiautomator2',
#                     'unicodeKeyboard': True,
#                     'resetKeyboard': True,
#                     'noReset': True,
#                     'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
#                     }
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # driver.implicitly_wait(10)
    # driver.find_element_by_id('com.tencent.mm:id/ij').click()
    #
    # # 生产
    # # self.driver.find_element_by_id('com.tencent.mm:id/ka').send_keys('众享亿家臻品好货')
    # # self.driver.find_element_by_id('com.tencent.mm:id/pp').click()
    # # self.driver.find_element_by_android_uiautomator('text(\"进入商城\")').click()
    #
    # # 测试
    # driver.find_element_by_id('com.tencent.mm:id/ka').send_keys('ceshi.zxyj.com')
    # driver.find_element_by_id('com.tencent.mm:id/pp').click()
    # driver.find_element_by_id('com.tencent.mm:id/bpg').click()
    #
    # # 切换到webview
    # time.sleep(5)
    # driver.switch_to.context(driver.contexts[1])

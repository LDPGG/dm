#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/19/019 14:39
# @Author  : 刘登攀
# @Site    : 
# @File    : wx.py
# @Software: PyCharm
from appium import webdriver


def ex():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'FJH5T18822042786',
        'appPackage': 'com.tencent.mm',
        'appActivity': '.ui.LauncherUI',
        'automationName': 'Uiautomator2',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    driver.find_element_by_accessibility_id('搜索').click()


if __name__ == '__main__':
    ex()
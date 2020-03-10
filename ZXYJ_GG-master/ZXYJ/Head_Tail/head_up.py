#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10/010 14:12
# @Author  : 刘登攀
# @Site    : 
# @File    : head_up.py
# @Software: PyCharm
from ZXYJ.Base.facility import *
from appium import webdriver


# 安卓微信启动头
def wechat_up():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': version_t(),
                    'deviceName': devices_t(),
                    'appPackage': 'com.tencent.mm',
                    'appActivity': '.ui.LauncherUI',
                    'automationName': 'Uiautomator2',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noReset': True,
                    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
                    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


# 众享亿家APP启动头
def app_up():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': devices_t(),
        'platformVersion': version_t(),
        'appPackage': 'com.tengchi.zxyjsc',
        'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    return desired_caps

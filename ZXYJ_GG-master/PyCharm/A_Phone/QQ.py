# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 0012 上午 11:41
# @Author  : 刘登攀阿！！
# @FileName: QQ.py
# @Software: PyCharm
from appium import webdriver
from time import sleep


def qq():
    print('开始运行')
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'bf18f20a',
        'platformVersion': '4.4.4',
        'appPackage': 'com.tengchi.zxyjsc',
        'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.find_element_by_id('com.tencent.mobileqq:id/name').click()
    sleep(1)
    driver.find_element_by_


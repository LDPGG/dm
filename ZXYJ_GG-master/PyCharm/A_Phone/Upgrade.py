# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 0005 上午 8:27
# @Author  : 刘登攀阿！！
# @FileName: Upgrade.py
# @Software: PyCharm
import unittest
import time
from selenium import webdriver
'''
购买升级礼包
'''


class Upgrade(unittest.TestCase):
    def ue(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '85GBCMD228AY',
            'platformVersion': '5.1',
            'appPackage': 'com.tengchi.zxyjsc',
            'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(8)
        # 点击首页，保证当前显示为首页
        driver.find_element_by_id('com.tengchi.zxyjsc:id/tabHomeLayout').click()
        time.sleep(1)
        # 定位到首页升级图标
        driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_vip').click()

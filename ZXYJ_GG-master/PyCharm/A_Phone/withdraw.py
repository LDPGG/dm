#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15/015 16:58
# @Author  : 刘登攀
# @Site    : 
# @File    : withdraw.py
# @Software: PyCharm
from appium import webdriver
import unittest
from BeautifulReport import BeautifulReport
from A_method.Slide import *
'''
众享豆操作
'''


class Withdraw(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'bf18f20a',
            'platformVersion': '4.4.4',
            'appPackage': 'com.tengchi.zxyjsc',
            'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 全局隐式等待20秒
        self.driver.implicitly_wait(20)

    # # 登录（看情况调用）
    # def enter_c(self):
    #     "密码正确登录测试"
    #     self.driver.find_element_by_android_uiautomator(u'text(\"跳过\")').click()
    #     try:
    #         self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()
    #     except:
    #         pass
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabMeLayout').click()
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_phone').send_keys(u'15386174586')
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_sign').send_keys(u'111111')
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_signin').click()

    # 提现
    def deposit(self):
        '账户提现测试'
        self.driver.find_element_by_android_uiautomator('text(\"跳过\")').click()
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()
        except:
            pass
        # 点击我，确保当前页面在我的界面
        self.driver.find_element_by_android_uiautomator('text(\"我\")').click()
        # 点击更多服务，进入众享豆界面
        self.driver.find_element_by_android_uiautomator('text(\"更多服务\")').click()
        # 点击兑换
        self.driver.find_element_by_android_uiautomator('text(\"兑换\")').click()
        # 输入兑换数量
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/etMoney').send_keys('100')
        # 点击下一步
        self.driver.find_element_by_android_uiautomator('text(\"下一步\")').click()
        # 输入支付密码
        self.driver.find_element_by_android_uiautomator('text(\"1\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"2\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"3\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"4\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"5\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"6\")').click()
        # 点击完成
        self.driver.find_element_by_android_uiautomator('text(\"完成\")').click()

    def increase(self):
        '账户转增测试'
        self.driver.find_element_by_android_uiautomator(u'text(\"跳过\")').click()
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()
        except:
            pass
        # 点击我，确保当前页面在我的界面
        self.driver.find_element_by_android_uiautomator('text(\"我\")').click()
        # 点击更多服务，进入众享豆界面
        self.driver.find_element_by_android_uiautomator('text(\"更多服务\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"转赠\")').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/phoneEt').send_keys('15831417766')
        self.driver.find_element_by_android_uiautomator('text(\"下一步\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"下一步\")').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/moneyEt').send_keys('100')
        self.driver.find_element_by_android_uiautomator('text(\"下一步\")').click()
        # 输入支付密码
        self.driver.find_element_by_android_uiautomator('text(\"1\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"2\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"3\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"4\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"5\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"6\")').click()
        # 点击完成
        self.driver.find_element_by_android_uiautomator('text(\"完成\")').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest = unittest.TestSuite()
    unittest.addTest(Withdraw('deposit'))
    unittest.addTest(Withdraw('increase'))
    br = BeautifulReport(unittest)
    br.report(filename='众享豆测试',
              description='众享豆测试',
              log_path=route()
              )

# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 0004 下午 4:16
# @Author  : 刘登攀阿！！
# @FileName: Purchase.py
# @Software: PyCharm

from appium import webdriver
from PyCharm.A_method import Slide
import unittest
from BeautifulReport import BeautifulReport
import time


class ZXYJ(unittest.TestCase):
    def setUp(self):
        print('开始测试')
        "购买产品测试"
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'DWH9X17106W08374',
            'platformVersion': '6.0',
            'appPackage': 'com.tengchi.zxyjsc',
            'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(8)

    def chase_01(self):
        '购买普通产品测试'
        # 定位搜索框
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/searchTv').click()
        # 定位输入框，并且输入产品名称
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/keywordEt').send_keys('高彪生抽')
        # 点击搜索按钮
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/cancelBtn').click()
        # 选中搜索列表的第一个产品
        try:
            self.driver.find_element_by_android_uiautomator('text(\"高彪生抽皇   \")').click()
        except:
            print('未找到预购买产品')
        # 购买
        self.driver.find_element_by_android_uiautomator('text(\"立即购买\")').click()
        print('找到预购买产品')
        # 确认购买
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        except:
            print('产品库存不足')
        # 滑动屏幕
        Slide.swipeUp(self.driver, 500, 1)
        # 选择余额支付
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/payBalanceTv').click()
        except:
            print('未找到对应的支付')
        # 确认付款
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        # 输入密码
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/password_edit_text').send_keys('123456')
        except:
            print('账户零钱不够')
        print('购买普通产品成功')

    def chase_02(self):
        '购买社群产品测试'
        # 定位搜索框
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/searchTv').click()
        # 定位输入框，并且输入产品名称
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/keywordEt').send_keys('自然堂活泉矿物补水保湿眼霜')
        # 点击搜索按钮
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/cancelBtn').click()
        # 选中搜索列表的第一个产品
        try:
            self.driver.find_element_by_android_uiautomator('text(\"¥90.00\")').click()
        except:
            print('未找到预购买产品')
        # 购买
        self.driver.find_element_by_android_uiautomator('text(\"立即购买\")').click()
        print('找到预购买产品')
        # 确认购买
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        except:
            print('产品库存不足')
        # 滑动屏幕
        Slide.swipeUp(self.driver, 500, 1)
        # 选择余额支付
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/payBalanceTv').click()
        except:
            print('未找到对应的支付')
        # 确认付款
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        # 输入密码
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/password_edit_text').send_keys('123456')
        except:
            print('账户零钱不够')
        print('购买社群产品成功')

    def chase_03(self):
        '购买秒杀产品测试'
        # 定位搜索框
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/searchTv').click()
        # 定位输入框，并且输入产品名称
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/keywordEt').send_keys('久居日用正品')
        # 点击搜索按钮
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/cancelBtn').click()
        # 选中搜索列表的第一个产品
        try:
            self.driver.find_element_by_android_uiautomator('text(\"¥34.00\")').click()
        except:
            print('未找到预购买产品')
        # 购买
        self.driver.find_element_by_android_uiautomator('text(\"立即购买\")').click()
        print('找到预购买产品')
        # 确认购买
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        except:
            print('产品库存不足')
        # 滑动屏幕
        Slide.swipeUp(self.driver, 500, 1)
        # 选择余额支付
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/payBalanceTv').click()
        except:
            print('未找到对应的支付')
        # 确认付款
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        # 输入密码
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/password_edit_text').send_keys('123456')
        except:
            print('账户零钱不够')
        print('购买秒杀产品成功')



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest = unittest.TestSuite()
    unittest.addTest(ZXYJ('chase_01'))
    unittest.addTest(ZXYJ('chase_02'))
    unittest.addTest(ZXYJ('chase_03'))
    br = BeautifulReport(unittest)
    br.report(filename='购买商品测试',
              description='购买商品测试',
              log_path='E:\dm\PyCharm\A_TestReport')

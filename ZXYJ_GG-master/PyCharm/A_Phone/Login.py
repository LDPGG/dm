# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 0003 下午 4:01
# @Author  : 刘登攀阿！！
# @FileName: Login.py
# @Software: PyCharm
from appium import webdriver
import unittest
from BeautifulReport import BeautifulReport

'''
登录脚本
'''


class Login(unittest.TestCase):
    def setUp(self):
        print('开始测试')
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '141acaef',
            'platformVersion': '7.1.1',
            'appPackage': 'com.tengchi.zxyjsc',
            'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def enter_a(self):
        "账号不存在登录测试"
        # self.driver.find_element_by_android_uiautomator(u'text(\"跳过\")').click()
        # self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabMeLayout').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_phone').send_keys(u'15858584586')
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_sign').send_keys(u'123456')
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_signin').click()

    def enter_b(self):
        "密码错误登录测试"
        # self.driver.find_element_by_android_uiautomator(u'text(\"跳过\")').click()
        # self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabMeLayout').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_phone').send_keys(u'15386174586')
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_sign').send_keys(u'123456')
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_signin').click()

    def enter_c(self):
        "密码正确登录测试"
        # self.driver.find_element_by_android_uiautomator(u'text(\"跳过\")').click()
        # self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabMeLayout').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_phone').send_keys(u'15386174586')
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_sign').send_keys(u'111111')
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_signin').click()

    def tearDown(self):
        self.driver.quit()
        print('测试结束')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login('enter_a'))
    suite.addTest(Login('enter_b'))
    suite.addTest(Login('enter_c'))
    result = BeautifulReport(suite)
    result.report(filename='APP测试报告',
                  description='测试报告',
                  log_path='E:\dm\PyCharm\A_TestReport')


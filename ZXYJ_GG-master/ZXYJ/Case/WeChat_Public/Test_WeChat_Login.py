#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4/004 9:40
# @Author  : 刘登攀
# @Site    : 
# @File    : Test_WeChat_Login.py
# @Software: PyCharm

from appium import webdriver
from ZXYJ.Head_Tail.head_up import *
import time
import unittest
import win32api
import win32con
import warnings


'''
微信密码登陆与验证码登录测试
'''


class WeChat(unittest.TestCase):
    # 进入商城
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', wechat_up)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.tencent.mm:id/iq').click()


        # 生产
        # self.driver.find_element_by_id('com.tencent.mm:id/ka').send_keys('众享亿家臻品好货')
        # self.driver.find_element_by_id('com.tencent.mm:id/pp').click()
        # self.driver.find_element_by_android_uiautomator('text(\"进入商城\")').click()

        self.driver.find_element_by_id('com.tencent.mm:id/kh').send_keys('ceshi.zxyj.com')
        self.driver.find_element_by_id('com.tencent.mm:id/q0').click()
        self.driver.find_element_by_id('com.tencent.mm:id/brd').click()

        # 切换到webview
        time.sleep(5)
        print(self.driver.contexts[1])
        self.driver.switch_to.context(self.driver.contexts[1])

    # 免密登录
    def code(self, phone, yzm):
        # 点击我
        self.driver.find_element_by_xpath('//*[@id="main-tab-top"]/div[4]/div[2]').click()
        print('成功跳转【我】页面\n')
        time.sleep(1)
        # 我是店主
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/button').click()
        # 点击免密登陆
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div/div/span[2]').click()
        # 输入手机号
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/li[2]/input').send_keys(phone)
        print('免密登陆跳转成功\n')
        print('手机号输入完成\n')
        # 点击发送获取验证码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/li[3]/button').click()
        print('验证码发送完成\n')
        # 填写验证码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/li[3]/input').send_keys(yzm)
        print('验证码填写完成\n')

    # 密码登录
    def landing(self, phone, dw):
        # 点击我
        self.driver.find_element_by_xpath('//*[@id="main-tab-top"]/div[4]/div[2]').click()
        print('成功跳转【我】页面')
        time.sleep(1)
        # 我是店主
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/button').click()
        # 输入手机号
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/ul/li/input').send_keys(phone)
        print('登录页面跳转完成')
        # 输入密码
        print('账户输入成功')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/ul/li[2]/input').send_keys(dw)
        # 点击登录
        print('密码输入完成')

# ------------------------------------测试用例-----------------------------------------------------------------

    # 手机号为空发送验证码
    def test_hmwk(self):
        "手机号为空发送验证码"
        WeChat.code(self, phone='', yzm='')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/button').click()
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/span').text, '手机号码不能为空')
        print('手机号为空,无法获取验证码')

    # 验证码错误
    def test_yzmcw(self):
        "验证码错误登陆"
        WeChat.code(self, phone='15386174586', yzm='1234')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/button').click()
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/span').text, '验证码出错！')
        print('验证码错误，登录失败')

    # 验证码未填写
    def text_yzmwk(self):
        "验证码为空登陆"
        WeChat.code(self, phone='15386174586', yzm='')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/button').click()
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/span').text, '验证码出错！')
        print('验证码为空，登录失败')

    # 验证码正确登陆
    def test_zqdl(self):
        "验证码正确登陆"
        WeChat.code(self, phone='15386174586', yzm='20160920')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[8]/ul/button').click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="main-tab-top"]/div[1]/div[2]'), '异常失败：登录失败')
        print('登录成功')
        win32api.MessageBox(0, "查看手机，退出当前账户后点击确认", "谢谢合作", win32con.MB_ICONASTERISK)

    # 密码错误
    def test_cwmm(self):
        "密码错误登录"
        WeChat.landing(self, phone='15386174586', dw='111111')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/ul/button').click()
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[4]/span').text, '密码有误.')
        print('密码错误，登陆失败')

    # 密码为空
    def test_mmwk(self):
        "密码为空登录"
        WeChat.landing(self, phone='15386174586', dw='')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/ul/button').click()
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[4]/span').text, '密码有误.')
        print('密码为空，登录失败')

    # 登录成功
    def test_zcdl(self):
        "登录成功"
        WeChat.landing(self, phone='15386174586', dw='123456')
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/ul/button').click()
        time.sleep(2)
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="main-tab-top"]/div[1]/div[2]').text, '异常失败：登录失败')
        print('登录成功')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

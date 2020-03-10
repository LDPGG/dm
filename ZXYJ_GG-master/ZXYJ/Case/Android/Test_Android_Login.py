#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11/011 13:52
# @Author  : 刘登攀
# @Site    : 
# @File    : Test_Android_Login.py
# @Software: PyCharm
import warnings
from ZXYJ.Head_Tail.head_up import *
from ZXYJ.Base.get_time import *
import unittest
from ZXYJ.Base.method import *


class Login(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        # 启动安卓APP

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', app_up())
        # 全局隐性等待20秒
        self.driver.implicitly_wait(20)
        # 关闭弹窗
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/ivClose').click()

    # # 登陆
    # def test_a_operate(self):
    #     # 输出写入日志
    #     print(get_time_up('登录'))
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabCartLayout').click()
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_phone').send_keys('15386174586')
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_sign').send_keys('111111')
    #     self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_signin').click()
    #     # 断言是否登陆成功
    #     self.assertIsNotNone(self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabHomeLayout'), '登录失败')
    #     # 输出写入日志
    #     print(get_time_quit('登录'))

    # 购买
    def test_b_buy(self):
        # 输出写入日志
        print(get_time_up('零钱购买流程'))
        # 确定搜索框
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/searchTv').click()
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/keywordEt').send_keys('测试')
        # 搜索产品
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/cancelBtn').click()
        # 选择搜索列表的第一个产品
        self.driver.find_element_by_name('这是后台测试的产品，请不要动').click()
        try:
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_action2').click()
        except:
            print(ero_test('定位购买按钮失败'))
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        try:
            # 进入地址选择
            self.driver.find_element_by_id('com.tengchi.zxyjsc:id/selectAddressTv').click()
        except:
            print(ero_test('产品库存不足'))
        # 选中地址
        self.driver.find_element_by_name('我结婚的').click()
        # 滑动屏幕
        swipe_down(self.driver, 500, 1)
        # 选择零钱
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/payBalanceTv').click()
        # 确认付款
        self.driver.find_element_by_id('com.tengchi.zxyjsc:id/confirmBtn').click()
        # 输入支付密码
        try:
            z_zfmm(self.driver)
        except:
            print(ero_test('零钱不足'))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

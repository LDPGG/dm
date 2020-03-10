# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 0023 下午 4:28
# @Author  : 刘登攀阿！！
# @FileName: AddChange.py
# @Software: PyCharm
'''
添加零钱
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import unittest
import HTMLTestRunner
from PyCharm.PyCharm.A_method.Slide import *


class Add(unittest.TestCase):
    """完整添加零钱"""
    def setUp(self):
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 网址
        self.driver.get("http://39.108.195.48:8080/flyweb/user/login")
        self.driver.implicitly_wait(30)

    def add_sq(self):
        """添加零钱申请测试"""
        # 调用登录方法
        login(driver=self.driver, username='admin', passwd='123456')
        time.sleep(2)
        # 添加零钱申请
        self.driver.find_element_by_xpath("//a[@href='333']").click()
        time.sleep(2)
        self.driver.find_element_by_id('btn99').click()
        time.sleep(2)
        self.driver.switch_to.frame('mainFrame')
        # send_keys后加要添加零钱的用户电话
        self.driver.find_element_by_id('keys').send_keys('15386174586')
        self.driver.find_element_by_xpath('//*[@id="search_order_form"]/div/div[3]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="orderlist"]/tbody/tr[2]/td[9]/button').click()
        time.sleep(2)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        sel = self.driver.find_element_by_id('type')
        # 加零钱（加：6  减：7）
        Select(sel).select_by_index()
        time.sleep(1)
        # 增加的钱
        self.driver.find_element_by_id('newMoney').send_keys('1000')
        # 填写备注
        self.driver.find_element_by_id('changeReason').send_keys('自动添加')
        # 切出ifram
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('modal-ok-btn').click()
        time.sleep(2)

    def add_sh(self):
        """零钱申请通过测试"""
        login(driver=self.driver, username='admin', passwd='123456')
        time.sleep(2)
        # 审核零钱
        # 切换列表
        self.driver.find_element_by_xpath('//*[@id="main-menu"]/li[6]/a').click()
        time.sleep(2)
        self.driver.find_element_by_id('btn146').click()
        self.driver.switch_to.frame('main-frame')
        self.driver.find_element_by_id('userPhone').send_keys('15386174586')
        self.driver.find_element_by_xpath('//*[@id="search_order_form"]/div/div[4]/button[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="checkboxList"]/tr[2]/td[8]/button[1]').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 执行用例
    testunit.addTest(Add("add_sq"))
    testunit.addTest(Add("add_sh"))
    # fliename = route('result.html')
    fp = open('result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告',
                                           description='测试执行情况')
    runner.run(testunit)
    fp.close()

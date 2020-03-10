# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 0024 下午 5:47
# @Author  : 刘登攀阿！！
# @FileName: XgYhDj.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import unittest
import HTMLTestRunner
from A_method.Slide import *
'''
修改结算等级
'''


class ZXYJ(unittest.TestCase):
    def setUp(self):
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 网址
        self.url = 'http://39.108.195.48:8080/flyweb/user/login'
        self.accept_next_alert = True

    def add_dl(self):
        "后台用户登录测试"
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('passwd').send_keys('123456')
        driver.find_element_by_id('submit_login').click()
        time.sleep(2)

    def add_js(self):
        driver = self.driver
        driver.get(self.url)
        "修改结算等级"
        # 账户密码登录
        # 抛出异常
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('passwd').send_keys('123456')
        driver.find_element_by_id('submit_login').click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@href='333']").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="btn72"]').click()
        time.sleep(1)
        driver.switch_to.frame('mainFrame')
        driver.find_element_by_id('keys').send_keys('15386174586')
        driver.find_element_by_xpath('//*[@id="search_order_form"]/div/div[3]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="orderlist"]/tbody/tr[2]/td[9]/button').click()
        time.sleep(1)
        # 切出
        driver.switch_to.default_content()
        # 切入
        driver.switch_to.frame('modal-frame')
        sel = driver.find_element_by_id('newMemberType')
        Select(sel).select_by_value('5')
        # 切出
        driver.switch_to.default_content()
        driver.find_element_by_id('modal-ok-btn').click()
        time.sleep(1)
        driver.quit()

    # 修改用户等级
    def add_dj(self):
        driver = self.driver
        driver.get(self.url)
        # 账户密码登录
        # 抛出异常
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('passwd').send_keys('123456')
        driver.find_element_by_id('submit_login').click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@href='333']").click()
        time.sleep(2)
        driver.find_element_by_id("btn83").click()
        time.sleep(1)
        # 切入
        driver.switch_to.frame('main-frame')
        driver.find_element_by_id('keys').send_keys('15386174586')
        driver.find_element_by_xpath('//*[@id="search_order_form"]/div/div[3]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="orderlist"]/tbody/tr[2]/td[9]/button').click()
        # 切出
        driver.switch_to.default_content()
        # 切入
        driver.switch_to.frame('modal-frame')
        sel1 = driver.find_element_by_id('newMemberGrade')
        Select(sel1).select_by_value('4')
        time.sleep(1)
        # 切出
        driver.switch_to.default_content()
        driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(ZXYJ("add_dl"))
    testunit.addTest(ZXYJ("add_js"))
    testunit.addTest(ZXYJ("add_dj"))
    fliename = route('result.html')
    fp = open(fliename, 'wb')
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          title='测试报告',
                                          description='测试执行情况')
    runer.run(testunit)
    fp.close()










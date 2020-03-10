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
from PyCharm.A_method.Slide import *

'''
会员等级修改
'''


class ZXYJ(unittest.TestCase):
    "会员等级结算修改"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "http://39.108.195.48:8080/flyweb/user/login"

    def add_js(self):
        "修改结算等级"
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
        # 修改结算等级0,3,5
        Select(sel).select_by_value('5')
        # 切出
        driver.switch_to.default_content()
        driver.find_element_by_id('modal-ok-btn').click()
        time.sleep(1)
        driver.quit()

    def add_dj(self):
        "修改会员等级"
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
        # 修改会员等级（0-7）
        Select(sel1).select_by_value('5')
        time.sleep(1)
        # 切出
        driver.switch_to.default_content()
        driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(ZXYJ("add_js"))
    testunit.addTest(ZXYJ("add_dj"))
    fliename = route('xg.html')
    fp = open(fliename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='ceshi', description='ylzx')
    runner.run(testunit)
    fp.close()









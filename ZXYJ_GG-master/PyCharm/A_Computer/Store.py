# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 0006 上午 10:58
# @Author  : 刘登攀阿！！
# @FileName: Store.py
# @Software: PyCharm
from selenium import webdriver
from A_method.Slide import *
import unittest
import time
import HTMLTestRunner
from selenium.webdriver.support.ui import Select
'''
店铺满活动自动化测试脚本
'''


class Store(unittest.TestCase):
    "店铺满活动测试"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://39.108.195.48:8080/flyweb/user/login')

    # 店铺满减测试
    def subtract(self):
        "店铺满减测试"
        login(driver=self.driver, username='admin', passwd='123456')
        time.sleep(2)
        # 店铺管理
        self.driver.find_element_by_xpath('//*[@id="main-menu"]/li[13]').click()
        time.sleep(1)
        # 店铺列表
        self.driver.find_element_by_id('btn18').click()
        time.sleep(1)
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 调用输入框方法
        store(driver=self.driver, choice='乐美苏泊尔')
        self.driver.find_element_by_xpath('/html/body/div[4]/ul').click()
        # 点击搜索
        self.driver.find_element_by_xpath('//*[@id="search_dealer_form"]/div/div[5]/button').click()
        time.sleep(1)
        # 点击店铺活动
        self.driver.find_element_by_xpath('//*[@id="dealerlist"]/tbody/tr[2]/td[12]/a[6]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 添加活动
        self.driver.find_element_by_xpath('/html/body/div/input[2]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 填写活动标题
        self.driver.find_element_by_xpath('//*[@id="noticeName"]').send_keys('自动化测试满减')
        time.sleep(1)
        # 填写满减价值
        self.driver.find_element_by_xpath('//*[@id="cost"]').send_keys('40')
        time.sleep(1)
        # 选择活动类型
        sel = self.driver.find_element_by_xpath('//*[@id="type"]')
        Select(sel).select_by_value('0')
        time.sleep(1)
        # 使用满减条件
        self.driver.find_element_by_xpath('//*[@id="minOrderMoney"]').send_keys('100')
        time.sleep(1)
        # 有限开始时间
        self.driver.find_element_by_xpath('//*[@id="startDate"]').send_keys('2018-09-06 14:27:00')
        self.driver.find_element_by_xpath('//*[@id="startDate"]').click()
        time.sleep(1)
        # 有限结束时间
        self.driver.find_element_by_xpath('//*[@id="endDate"]').send_keys('2018-10-31 22:26:59')
        self.driver.find_element_by_xpath('//*[@id="endDate"]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 确定
        self.driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(1)
        # 查找设置好的满减活动
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 输入搜索条件
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('自动化测试满减')
        time.sleep(1)
        # 点击查找
        self.driver.find_element_by_xpath('//*[@id="search_dealer_form"]/div/div[3]/button').click()
        time.sleep(1)
        # 编辑活动
        self.driver.find_element_by_xpath('//*[@id="dealerlist"]/tbody/tr[2]/td[10]/a[1]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 点击增加客户端
        self.driver.find_element_by_xpath('//*[@id="addactivityTerminal"]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 开启状态
        status = self.driver.find_element_by_xpath('//*[@id="terminal"]')
        # 安卓
        Select(status).select_by_value('1')
        time.sleep(1)
        # 苹果
        # Select(status).select_by_value('2')
        # 微信
        # Select(status).select_by_value('3')
        # 切出
        self.driver.switch_to.default_content()
        # 确定
        self.driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(1)
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 限制参与次数(默认无限次)
        # self.driver.find_element_by_xpath('//*[@id="terminal"]/tbody/tr/td[3]/input').send_keys()
        # time.sleep(1)
        # 开关
        self.driver.find_element_by_xpath('//*[@id="terminal"]/tbody/tr/td[6]/div/i').click()
        time.sleep(1)

    # 店铺满送测试
    def Send(self):
        "店铺满送测试"
        login(driver=self.driver, username='admin', passwd='123456')
        time.sleep(2)
        # 店铺管理
        self.driver.find_element_by_xpath('//*[@id="main-menu"]/li[13]').click()
        time.sleep(1)
        # 店铺列表
        self.driver.find_element_by_id('btn18').click()
        time.sleep(1)
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 调用输入框方法
        store(driver=self.driver, choice='乐美苏泊尔')
        self.driver.find_element_by_xpath('/html/body/div[4]/ul').click()
        # 点击搜索
        self.driver.find_element_by_xpath('//*[@id="search_dealer_form"]/div/div[5]/button').click()
        time.sleep(1)
        # 点击店铺活动
        self.driver.find_element_by_xpath('//*[@id="dealerlist"]/tbody/tr[2]/td[12]/a[6]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 添加活动
        self.driver.find_element_by_xpath('/html/body/div/input[2]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 填写活动标题
        self.driver.find_element_by_xpath('//*[@id="noticeName"]').send_keys('自动化测试满送')
        time.sleep(1)
        # 填写满减价值
        self.driver.find_element_by_xpath('//*[@id="cost"]').send_keys('40')
        time.sleep(1)
        # 选择活动类型
        sel = self.driver.find_element_by_xpath('//*[@id="type"]')
        Select(sel).select_by_value('3')
        time.sleep(1)
        # 使用满减条件
        self.driver.find_element_by_xpath('//*[@id="minOrderMoney"]').send_keys('100')
        time.sleep(1)
        # 有限开始时间
        self.driver.find_element_by_xpath('//*[@id="startDate"]').send_keys('2018-09-06 14:27:00')
        self.driver.find_element_by_xpath('//*[@id="startDate"]').click()
        time.sleep(1)
        # 有限结束时间
        self.driver.find_element_by_xpath('//*[@id="endDate"]').send_keys('2018-10-31 22:26:59')
        self.driver.find_element_by_xpath('//*[@id="endDate"]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 确定
        self.driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(1)
        # 查找设置好的满减活动
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 输入搜索条件
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('自动化测试满送')
        time.sleep(1)
        # 点击查找
        self.driver.find_element_by_xpath('//*[@id="search_dealer_form"]/div/div[3]/button').click()
        time.sleep(1)
        # 编辑活动
        self.driver.find_element_by_xpath('//*[@id="dealerlist"]/tbody/tr[2]/td[10]/a[1]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 点击增加客户端
        self.driver.find_element_by_xpath('//*[@id="addactivityTerminal"]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 开启状态
        status = self.driver.find_element_by_xpath('//*[@id="terminal"]')
        # 苹果
        Select(status).select_by_value('2')
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 确定
        self.driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(1)
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 限制参与次数(默认无限次)
        # self.driver.find_element_by_xpath('//*[@id="terminal"]/tbody/tr/td[3]/input').send_keys()
        # time.sleep(1)
        # 关联产品
        self.driver.find_element_by_xpath('//*[@id="brandlist"]/tbody/tr[2]/td[15]/a').click()
        time.sleep(2)
        # 开关
        self.driver.find_element_by_xpath('//*[@id="terminal"]/tbody/tr/td[6]/div/i').click()
        time.sleep(1)

    # 店铺满赠测试
    def present(self):
        "店铺满赠测试"
        login(driver=self.driver, username='admin', passwd='123456')
        time.sleep(2)
        # 店铺管理
        self.driver.find_element_by_xpath('//*[@id="main-menu"]/li[13]').click()
        time.sleep(1)
        # 店铺列表
        self.driver.find_element_by_id('btn18').click()
        time.sleep(1)
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 调用输入框方法
        store(driver=self.driver, choice='乐美苏泊尔')
        self.driver.find_element_by_xpath('/html/body/div[4]/ul').click()
        # 点击搜索
        self.driver.find_element_by_xpath('//*[@id="search_dealer_form"]/div/div[5]/button').click()
        time.sleep(1)
        # 点击店铺活动
        self.driver.find_element_by_xpath('//*[@id="dealerlist"]/tbody/tr[2]/td[12]/a[6]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 添加活动
        self.driver.find_element_by_xpath('/html/body/div/input[2]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 填写活动标题
        self.driver.find_element_by_xpath('//*[@id="noticeName"]').send_keys('自动化测试满赠')
        time.sleep(1)
        # 填写满减价值
        self.driver.find_element_by_xpath('//*[@id="cost"]').send_keys('40')
        time.sleep(1)
        # 选择活动类型
        sel = self.driver.find_element_by_xpath('//*[@id="type"]')
        Select(sel).select_by_value('1')
        time.sleep(1)
        # 使用满减条件
        self.driver.find_element_by_xpath('//*[@id="minOrderMoney"]').send_keys('100')
        time.sleep(1)
        # 有限开始时间
        self.driver.find_element_by_xpath('//*[@id="startDate"]').send_keys('2018-09-06 14:27:00')
        self.driver.find_element_by_xpath('//*[@id="startDate"]').click()
        time.sleep(1)
        # 有限结束时间
        self.driver.find_element_by_xpath('//*[@id="endDate"]').send_keys('2018-10-31 22:26:59')
        self.driver.find_element_by_xpath('//*[@id="endDate"]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 确定
        self.driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(1)
        # 查找设置好的满减活动
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 输入搜索条件
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('自动化测试满赠')
        time.sleep(1)
        # 点击查找
        self.driver.find_element_by_xpath('//*[@id="search_dealer_form"]/div/div[3]/button').click()
        time.sleep(1)
        # 编辑活动
        self.driver.find_element_by_xpath('//*[@id="dealerlist"]/tbody/tr[2]/td[10]/a[1]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 点击增加客户端
        self.driver.find_element_by_xpath('//*[@id="addactivityTerminal"]').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 开启状态
        status = self.driver.find_element_by_xpath('//*[@id="terminal"]')
        # 苹果
        Select(status).select_by_value('2')
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 确定
        self.driver.find_element_by_xpath('//*[@id="modal-ok-btn"]').click()
        time.sleep(1)
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 限制参与次数(默认无限次)
        # self.driver.find_element_by_xpath('//*[@id="terminal"]/tbody/tr/td[3]/input').send_keys()
        # time.sleep(1)
        # 点击添加优惠券
        self.driver.find_element_by_xpath('/html/body/div[1]/input[5]').click()
        time.sleep(1)
        # 填写优惠券信息
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 选择优惠券类型
        coupon = self.driver.find_element_by_xpath('//*[@id="couponType"]')
        Select(coupon).select_by_value('1')
        time.sleep(1)
        # 输入优惠券的标题
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('自动化测试专用优惠券')
        time.sleep(1)
        # 输入优惠券金额
        self.driver.find_element_by_xpath('//*[@id="cost"]').send_keys('50')
        time.sleep(1)
        # 输入订单满足金额
        self.driver.find_element_by_xpath('//*[@id="minOrderMoney"]').send_keys('100')
        time.sleep(1)
        # 输入优惠券库存
        self.driver.find_element_by_xpath('//*[@id="stock"]').send_keys('999')
        time.sleep(1)
        # 优惠券开始使用时间
        self.driver.find_element_by_xpath('//*[@id="startDate"]').send_keys('2018-09-06 14:27:00')
        self.driver.find_element_by_xpath('//*[@id="startDate"]').click()
        time.sleep(1)
        # 有限结束时间
        self.driver.find_element_by_xpath('//*[@id="endDate"]').send_keys('2018-10-31 22:26:59')
        self.driver.find_element_by_xpath('//*[@id="endDate"]').click()
        # 选择图片
        self.driver.find_element_by_id('thumbUrlbanner').click()
        time.sleep(5)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('modal-frame')
        # 点击选择图片
        self.driver.find_element_by_id('findImgName').send_keys('133')
        # 搜索图片
        self.driver.find_element_by_xpath('//*[@id="top"]/li[4]/button').click()
        time.sleep(3)
        # 选中图片
        self.driver.find_element_by_id('divcd9e6bdabfda4c07a762c81f9a5bdfce').click()
        time.sleep(3)
        # 切出
        self.driver.switch_to.default_content()
        # 确定图片
        self.driver.find_element_by_id('modal-ok-btn').click()
        time.sleep(5)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath('//*[@id="addProduct"]/tbody/tr[11]/td[2]/input').click()
        time.sleep(1)
        # 切出
        self.driver.switch_to.default_content()
        # 切入
        self.driver.switch_to.frame('mainFrame')
        # 搜索优惠券
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('自动化测试专用优惠券')
        time.sleep(1)
        # 点击搜索
        self.driver.find_element_by_xpath('//*[@id="search_brand_form"]/div/div[3]/button').click()
        time.sleep(1)
        # 点击关联
        self.driver.find_element_by_xpath('//*[@id="brandlist"]/tbody/tr[2]/td[12]/a[1]').click()
        time.sleep(1)
        # 开关
        self.driver.find_element_by_xpath('//*[@id="terminal"]/tbody/tr/td[6]/div/i').click()
        time.sleep(1)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Store("subtract"))
    testunit.addTest(Store("Send"))
    testunit.addTest(Store("present"))
    fliename = route('TestStora.html')
    fp = open(fliename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='店铺满活动自动化测试用例', description='用例执行情况')
    runner.run(testunit)
    fp.close()

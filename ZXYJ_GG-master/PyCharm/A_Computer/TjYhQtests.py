# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 0030 下午 2:05
# @Author  : 刘登攀阿！！
# @FileName: TjYhQtests.py
# @Software: PyCharm

'''
添加优惠券
'''
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from BeautifulReport import BeautifulReport


class AddClass(unittest.TestCase):
    "添加优惠券测试"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'http://39.108.195.48:8080/flyweb/user/login'

    def ADD(self):
        "添加优惠券"
        driver = self.driver
        driver.get(self.url)
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get('http://39.108.195.48:8080/flyweb/user/login')
        # 账号
        driver.find_element_by_xpath("//input[@id='username']").send_keys('admin')
        # 密码
        driver.find_element_by_xpath("//input[@id='passwd']").send_keys('123456')
        driver.find_element_by_xpath("//a[@id='submit_login']").click()
        # 停顿一秒
        time.sleep(1)
        # 选择产品管理
        driver.find_element_by_xpath("//a[@href='product/list']").click()
        time.sleep(1)
        # 选择优惠券管理
        driver.find_element_by_xpath("//a[@href='../product/couponList?menuId=168']").click()
        time.sleep(1)
        # 切入
        driver.switch_to.frame('mainFrame')
        # 添加优惠券
        driver.find_element_by_xpath('/html/body/div/input').click()
        time.sleep(1)
        # 切出
        driver.switch_to.default_content()
        # 切入
        driver.switch_to.frame('mainFrame')
        # 选择优惠券类型
        sel = driver.find_element_by_id('couponType')
        # 指定产品可以优惠券0  店铺满减优惠券1
        Select(sel).select_by_value('1')
        time.sleep(5)
        # 优惠券标题
        driver.find_element_by_id('title').send_keys('脚本添加')
        time.sleep(5)
        # 选择店铺
        sel1 = driver.find_element_by_id('storeId')
        Select(sel1).select_by_value('65a8ae92d17442bf91bcb52431406c18')
        time.sleep(1)
        # 优惠券的金额
        driver.find_element_by_id('cost').send_keys('50')
        time.sleep(5)
        # 优惠券的使用条件
        driver.find_element_by_id('minOrderMoney').send_keys('100')
        time.sleep(5)
        # 优惠券的库存
        driver.find_element_by_id('stock').send_keys('999')
        time.sleep(5)
        # 选择图片
        driver.find_element_by_id('thumbUrlbanner').click()
        time.sleep(5)
        # 切出
        driver.switch_to.default_content()
        # 切入
        driver.switch_to.frame('modal-frame')
        # 点击选择图片
        driver.find_element_by_id('findImgName').send_keys('133')
        # 搜索图片
        driver.find_element_by_xpath('//*[@id="top"]/li[4]/button').click()
        time.sleep(5)
        # 选中图片
        driver.find_element_by_id('divcd9e6bdabfda4c07a762c81f9a5bdfce').click()
        time.sleep(5)
        # 切出
        driver.switch_to.default_content()
        # 确定图片
        driver.find_element_by_id('modal-ok-btn').click()
        time.sleep(5)
        # 切入
        driver.switch_to.frame('mainFrame')
        # 优惠券开始使用时间
        driver.find_element_by_id('startDate').send_keys('2018-09-01 01:00:00')
        time.sleep(1)
        # 取消时间框
        driver.find_element_by_id('startDate').click()
        time.sleep(1)
        # 优惠券结束使用时间
        driver.find_element_by_id('endDate').send_keys('2018-09-30 23:59:00')
        time.sleep(1)
        # 取消时间框
        driver.find_element_by_id('endDate').click()
        time.sleep(1)
        # 优惠券开始领取时间
        driver.find_element_by_id('starttime').send_keys('2018-09-01 01:00:00')
        time.sleep(1)
        # 取消时间框
        driver.find_element_by_id('starttime').click()
        time.sleep(1)
        # 优惠券结束领取时间
        driver.find_element_by_id('endtime').send_keys('2018-09-30 23:59:00')
        time.sleep(1)
        # 取消时间框
        driver.find_element_by_id('endtime').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="addProduct"]/tbody/tr[13]/td[2]/input').click()
        time.sleep(50)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # testunit.addTest(unittest.makeSuite(AddClass))
    testunit.addTest(AddClass('ADD'))
    result = BeautifulReport(testunit)
    result.report(filename='众享亿家测试用例',
                  description='添加优惠券测试用例',
                  log_path='.')
    # suite_tests = unittest.defaultTestLoader.discover('.',
    #                                                   pattern='TjYhQtests.py',
    #                                                   top_level_dir=None)
    # BeautifulReport(suite_tests).report(filename='众享亿家测试用例',
    #                                     description='添加优惠券测试用例',
    #                                     log_path='.')
    # fliename = route('yhqces.html')
    # fp = open(fliename, 'wb')
    # runer = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                       title='添加优惠券测试',
    #                                       description='测试执行情况')
    # runer.run(testunit)
    # fp.close()

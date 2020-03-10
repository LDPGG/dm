#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7/007 16:55
# @Author  : 刘登攀
# @Site    : 
# @File    : Test_WeChat_Buy.py
# @Software: PyCharm
from BeautifulReport import BeautifulReport
from appium import webdriver
from ZXYJ.Head_Tail.head_up import *
from ZXYJ.Base.facility import *
import warnings
import time
import unittest
from appium.webdriver.common.touch_action import TouchAction

'''
微信端购买产品测试
1.普通产品
2.社群团购产品
3.秒杀产品
4.海外购产品（暂未考虑清楚到底是否需要）
'''


class Buy(unittest.TestCase):
    # 进入商城
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', wechat_up())
        self.driver.implicitly_wait(30)

        # 微信搜索
        # self.driver.find_element_by_id('com.tencent.mm:id/ij').click()
        #
        #         # 生产
        #         # self.driver.find_element_by_id('com.tencent.mm:id/ka').send_keys('众享亿家臻品好货')
        #         # self.driver.find_element_by_id('com.tencent.mm:id/pp').click()
        #         # self.driver.find_element_by_android_uiautomator('text(\"进入商城\")').click()
        #
        #         # 测试
        #         # self.driver.find_element_by_id('com.tencent.mm:id/ij').click()
        #         time.sleep(10)
        #         # TouchAction(self.driver).press(x=550, y=100).release().perform()
        #         # self.driver.find_element_by_id('com.tencent.mm:id/ka').send_keys('ceshi.zxyj.com')
        #         # self.driver.find_element_by_id('com.tencent.mm:id/pp').click()
        #         # self.driver.find_element_by_id('com.tencent.mm:id/bpg').click()
        #
        #         # # -------------------------------------
        #         # self.driver.find_element_by_id('com.tencent.mm:id/iq').click()
        #         # time.sleep(1)

        TouchAction(self.driver).press(x=550, y=100).release().perform()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/kh').send_keys('css')
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/q0').click()


        # 切换到webview
        time.sleep(8)
        print(self.driver.contexts[1])
        self.driver.switch_to.context(self.driver.contexts[1])

    # 挑选产品
    def txcp(self, cp):
        self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="search-field"]'), '异常失败：未找到产品搜索框')
        # 选中弹窗
        self.driver.find_element_by_xpath('//*[@id="search-field"]').click()
        time.sleep(1)
        # 输入产品名称
        self.driver.find_element_by_xpath('//*[@id="search-field"]').send_keys(cp)
        self.driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div[2]').click()
        print('产品名称：%s 输入完成' % cp)
        # 选择搜索结果的第一个产品
        time.sleep(4)
        self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="category"]/div[1]/div/div[2]/div[1]').text, cp, '异常失败：没有找到对应的产品')
        self.driver.find_element_by_xpath('//*[@id="category"]/div[1]/div').click()
        print('产品搜索完成')
        time.sleep(1)
        try:
            self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[9]/div[5]').text, '立即购买', '异常失败：没有检测到立即购买按钮')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[9]/div[5]').click()
        except:
            self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[10]/div[5]').text, '立即购买', '异常失败：没有检测到立即购买按钮')
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[10]/div[5]').click()
        print('成功进入产品详情页')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="product-sku"]/div[2]/div').click()
        print('成功创建订单')
        time.sleep(3)
        # 支付方式
        zffs(self.driver)
        self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="pay"]/div[5]/div[2]/div[2]').text, '确认付款', '异常失败：未检测到确认付款按钮')
        self.driver.find_element_by_xpath('//*[@id="pay"]/div[5]/div[2]/div[2]').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

# --------------------------------------用例在下面添加-----------------------------------------------------------------------------------------------

    # 普通产品（零钱充足）
    def test_common_cz(self):
        "购买普通产品(零钱充足)   预期结果：购买成功"
        Buy.txcp(self, '普通产品')
        # 输入支付密码
        Buy(self)
        time.sleep(1)
        self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="order-detail"]/div[2]/div[1]').text, '待发货', '异常失败：购买失败')
        print('购买成功')

    # 普通产品（零钱不足）
    def test_common_bz(self):
        "购买普通产品(零钱不足)   预期结果：购买失败"
        Buy.txcp(self, '普通产品')
        # 输入支付密码
        z_zfmm(self.driver)
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/span').text, '您的零钱不足', '异常失败：未检测到零钱不足提示')
        print('零钱不充足，购买失败')

    # 社群团购产品（零钱充足）
    def test_group_cz(self):
        "购买社群团购产品(零钱充足)    预期结果：购买成功"
        Buy.txcp(self, '社群产品')
        # 输入支付密码
        z_zfmm(self.driver)
        time.sleep(1)
        self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="order-detail"]/div[2]/div[1]').text, '待发货', '异常失败：购买失败')
        print('购买成功')

    # 社群产品（零钱不足）
    def test_group_bz(self):
        "购买社群产品(零钱不足)   预期结果：购买失败"
        Buy.txcp(self, '社群产品')
        # 输入支付密码
        z_zfmm(self.driver)
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/span').text, '您的零钱不足', '异常失败：未检测到零钱不足提示')
        print('零钱不充足，购买失败')

    # 秒杀产品（零钱充足）
    def test_seckill_cz(self):
        "购买秒杀产品(零钱充足)   预期结果：购买成功"
        Buy.txcp(self, '秒杀产品')
        # 输入支付密码
        z_zfmm(self.driver)
        time.sleep(1)
        self.assertIsNot(self.driver.find_element_by_xpath('//*[@id="order-detail"]/div[2]/div[1]').text, '待发货', '异常失败：购买失败')
        print('购买成功')

    # 社群产品（零钱不足）
    def test_seckill_bz(self):
        "购买秒杀产品(零钱不足)   预期结果：购买失败"
        Buy.txcp(self, '社群产品')
        # 输入支付密码
        z_zfmm(self.driver)
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/span').text, '您的零钱不足', '异常失败：未检测到零钱不足提示')
        print('实际结果：零钱不充足，购买失败')


if __name__ == '__main__':
    unittest.main()
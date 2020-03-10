#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17/017 14:56
# @Author  : 刘登攀
# @Site    : 
# @File    : element.py
# @Software: PyCharm
self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabMeLayout').click()
self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_phone').send_keys('15386174586')
self.driver.find_element_by_id('com.tengchi.zxyjsc:id/et_sign').send_keys('123456')
self.driver.find_element_by_id('com.tengchi.zxyjsc:id/btn_signin').click()
# 断言是否登陆成功
self.assertIsNotNone(self.driver.find_element_by_id('com.tengchi.zxyjsc:id/tabHomeLayout'), '登录失败')


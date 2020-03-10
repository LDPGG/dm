#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29/029 10:40
# @Author  : 刘登攀
# @Site    : 
# @File    : login.py
# @Software: PyCharm
import uiautomator2 as ui2
from ZXYJ.Base.facility import *
from time import sleep


def tets_log(self):
    # 获取测试手机
    self.devices = ui2.connect_usb(devices_t())
    # 启动APP
    self.devices.app_start('com.tengchi.zxyjsc')
    # 点击搜索框
    self.devices(resourceId='com.tengchi.zxyjsc:id/searchTv').click()
    sleep(2)
    # 输入搜索内容
    self.devices(resourceId='com.tengchi.zxyjsc:id/keywordEt').send_keys('苏泊尔')
    # 点击搜索按钮
    self.devices(resourceId='com.tengchi.zxyjsc:id/cancelBtn').click()
    self.devices.click(0.772, 0.311)
    sleep(10)
    self.devices.app_stop('com.tengchi.zxyjsc')


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10/010 10:55
# @Author  : 刘登攀
# @Site    : 
# @File    : facility.py
# @Software: PyCharm
import os
import re
import time


# 获文件路径
def location():
    side = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + '')
    return side


# 筛选‘test_’开头的测试用例
def path():
    side = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+'')
    reg = re.compile('Test_(.*?).py')
    site = []
    for root, dirs, files in os.walk(side + r'\Case\ui2'):
        for file in files:
            result = reg.match(file)
            if result:
                site.append(result.group())
    return site


# 检查设备，获取deviceName
def devices_t():
    devices_s = os.popen('adb devices').read()
    device_name = re.findall('(.*?)	device', devices_s)
    if device_name:
        return device_name[0]
    else:
        return '设备未连接'


# 获取platformVersion
def version_t():
    version = os.popen('adb shell getprop ro.build.version.release').read()
    if version:
        return version.replace('\n', '')
    else:
        return '没有发现设备/模拟器'


# 安装APP
def installer_app():
    cmd = r'adb install %s\APP\app-debug.apk' % location()
    os.popen(cmd).read()


# 选择支付方式
def zffs(driver):
    weizhi2 = driver.find_element_by_xpath('//*[@id="pay"]/div[4]/div[3]/div[2]/div[4]/div[2]')  # 先定位到一个元素
    driver.execute_script("arguments[0].scrollIntoView();", weizhi2)  # 让其滚动到这个坐标
    time.sleep(2)
    # 选中零钱支付
    driver.find_element_by_xpath('//*[@id="pay"]/div[4]/div[3]/div[2]/div[4]/div[2]').click()
    print('成功选中零钱支付')


# 正确支付密码
def z_zfmm(driver):
    # 1
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[1]/i[1]').click()
    # 2
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[1]/i[2]').click()
    # 3
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[1]/i[3]').click()
    # 4
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[2]/i[1]').click()
    # 5
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[2]/i[2]').click()
    # 6
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[2]/i[3]').click()


# 错误支付密码
def c_zfmm(driver):
    # 1
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[1]/i[1]').click()
    # 2
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[1]/i[2]').click()
    # 3
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[1]/i[3]').click()
    # 4
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[2]/i[1]').click()
    # 6
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[2]/i[3]').click()
    # 5
    driver.find_element_by_xpath('//*[@id="pay"]/div[7]/div/div[3]/div[2]/i[2]').click()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11/011 16:41
# @Author  : 刘登攀
# @Site    : 
# @File    : pet_name.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
'''
阿胖：获取昵称
'''

def entry():
    # 调用浏览器并窗口最大化
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get('https://qun.qq.com/member.html#gid=%s' % qqqq)
    driver.get('https://qun.qq.com/member.html#gid=131853242')
    # 全局隐式等待30秒
    driver.implicitly_wait(30)
    # 切入
    driver.switch_to.frame('login_frame')
    # 自动登录
    # driver.find_element_by_id('img_out_%s' % cece).click()
    driver.find_element_by_id('img_out_1583141776').click()
    # 切出
    driver.switch_to.default_content()
    time.sleep(6)
    # # 控制屏幕滑动，获取更多群员信息
    for ai in range(60):
        print(ai)
        if ai <= 60:
            driver.execute_script("window.scrollTo(0,50000)")
            ai += 10
            time.sleep(1)
    # 获取源码
    res = driver.page_source
    # 关闭浏览器
    driver.quit()
    # 将源代码存入txt文本
    with open(r'.html.txt', 'w', encoding='utf-8') as f:
        f.write(res)
    f.close()
    # 读取txt文本
    with open(r'.html.txt', 'r', encoding='utf-8') as f:
        res = f.read()
    # 遍历文档
    soup = BeautifulSoup(res, "html.parser")
    # # 取QQ号码
    # fall = soup.find_all(class_='td-user-nick')
    fall = soup.select('td span')
    a = re.findall('<span>(\s*.*?\s*)</span>', '%s' % fall)
    for i in range(len(a)):
        a[i] = a[i].replace('\r', '').replace('\n', '').replace('\t', '')
        with open(r'nicheng.txt', 'a', encoding='utf-8') as f:
            f.write(a[i] + '\n')
        f.close()


if __name__ == '__main__':
    entry()

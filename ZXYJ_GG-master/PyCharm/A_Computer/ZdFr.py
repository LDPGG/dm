# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 0025 上午 11:49
# @Author  : 刘登攀阿！！
# @FileName: ZdFr.py
# @Software: PyCharm
from selenium import webdriver
import time
'''
账号封禁
'''


def add_change():
    # yy = input('请输入封禁原因：')
    # 添加零钱申请
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    webdriver.Firefox()
    # 浏览器最大化
    driver.maximize_window()
    # 网址
    driver.get('http://39.108.195.48:8080/flyweb/user/login')
    # 账户密码登录
    # 抛出异常
    try:
        # 选填
        # driver.find_element_by_id('username').send_keys(zh)
        # driver.find_element_by_id('passwd').send_keys(mm)
        # # 固定
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('passwd').send_keys('123456')
        driver.find_element_by_id('submit_login').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main-menu"]/li[11]/a').click()
        time.sleep(2)
    except:
        print('您的账户或者密码错误，请重新输入！！')
        # 关闭浏览器
        driver.quit()
        # 回调方法
        add_change()
    driver.find_element_by_id('btn32').click()
#     切入
    driver.switch_to.frame('mainFrame')
    driver.find_element_by_id('keys').send_keys('15386174586')
    driver.find_element_by_xpath('//*[@id="search_order_form"]/div/div[2]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="orderlist"]/tbody/tr[2]/td[13]/button').click()
    time.sleep(2)
    # 切出
    driver.switch_to.default_content()
    # 切入
    driver.switch_to.frame('modal-frame')
    driver.find_element_by_id('startDate').send_keys('2333-03-03 03:33:00')
    driver.find_element_by_id('freezeReason').send_keys('1111')
    time.sleep(1)
    driver.switch_to.default_content()
    driver.find_element_by_id('modal-ok-btn').click()
    time.sleep(1)


def JF():
    # 添加零钱申请
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    # 浏览器最大化
    driver.maximize_window()
    # 网址
    driver.get('http://39.108.195.48:8080/flyweb/user/login')
    # 账户密码登录
    # 抛出异常
    try:
        # 选填
        # driver.find_element_by_id('username').send_keys(zh)
        # driver.find_element_by_id('passwd').send_keys(mm)
        # # 固定
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('passwd').send_keys('123456')
        driver.find_element_by_id('submit_login').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main-menu"]/li[11]/a').click()
        time.sleep(2)
    except:
        print('您的账户或者密码错误，请重新输入！！')
        # 关闭浏览器
        driver.quit()
        # 回调方法
        JF()
    driver.find_element_by_xpath('//*[@id="btn34"]/a').click()
    time.sleep(1)
    driver.switch_to.frame('mainFrame')
    driver.find_element_by_id('keys').send_keys(sj)
    driver.find_element_by_xpath('//*[@id="search_order_form"]/div/div[2]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="orderlist"]/tbody/tr[2]/td[13]/button').click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.find_element_by_id('modal-ok-btn').click()
    time.sleep(5)
    driver.quit()


def main():
    xz = input('冻结输1，解冻输2：')
    if xz == '1':
        add_change()
    elif xz == '2':
        JF()
    else:
        print('输入错误！')
        main()


if __name__ == '__main__':
    # zh = input('请输入您的后台账户：')
    # mm = input('请输入您的后台账户密码：')
    # sj = input('请输入要封禁/解封的手机号码：')
    main()
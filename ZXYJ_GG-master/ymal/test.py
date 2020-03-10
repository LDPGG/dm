#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18/018 16:17
# @Author  : 刘登攀
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    url = 'http://www.126.com'

    def __init__(self, selenium_driver, base_url=url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    url = '/'

    # 定位器
    username_loc = (By.ID, 'idInput')
    password_loc = (By.ID, 'pwdInput')
    submit_loc = (By.ID, 'loginBtn')

    # Action
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    """
    测试获取的用户名/密码是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()


def main():
    try:
        driver = webdriver.Chrome()
        username = 'admin'
        password = '123456'
        test_user_login(driver, username, password)
        sleep(3)
        text = driver.find_element_by_xpath("//span[@id='spanUid']").text
        assert (text == 'username@126.com'), '用户名称不匹配，登陆失败！'
    finally:
        driver.close()


if __name__ == '__main__':
    main()
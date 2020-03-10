# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 0014 下午 6:30
# @Author  : 刘登攀阿！！
# @FileName: Dog2.py
# @Software: PyCharm

from selenium import webdriver
# 这是我自己封装的一堆方法
from A_method.Slide import *
import unittest
import time
import HTMLTestRunner


class Store(unittest.TestCase):
    "测试"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')

    def su(self):
        self.driver.find_element_by_id('kw').send_keys('python')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Store('su'))
    # route 是我自己封装的文件路径，我把所有的测试报告都放在一个文件夹的，这里你自己可以改一下
    # fliename = route('tets.html')
    fp = open('tets.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试用例',
                                           description='用例执行情况')
    runner.run(testunit)
    fp.close()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18/018 10:28
# @Author  : 刘登攀
# @Site    : 
# @File    : get_time.py
# @Software: PyCharm
import time
'''
添加测试日志
'''


# 获取当前时间
def get_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time


# 开始测试日志
def get_time_up(name):
    doc = open(r'C:\Users\Administrator\Desktop\test_log.txt', 'a')
    print('=============================================\n--------------%s开始测试%s' % (get_time(), name), file=doc)
    doc.close()
    return '--------------%s开始测试%s' % (get_time(), name)


# 结束测试日志
def get_time_quit(name):
    doc = open(r'C:\Users\Administrator\Desktop\test_log.txt', 'a')
    print('--------------%s测试%s结束\n=============================================' % (get_time(), name), file=doc)
    doc.close()
    return '--------------%s测试%s结束' % (get_time(), name)


# 报错退出日志
def ero_test(name):
    doc = open(r'C:\Users\Administrator\Desktop\test_log.txt', 'a')
    print('-----报错日志:%s %s报错退出' % (get_time(), name), file=doc)
    doc.close()
    return '--------------报错日志:%s %s报错退出' % (get_time(), name)



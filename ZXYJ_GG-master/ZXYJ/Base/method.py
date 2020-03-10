#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18/018 10:02
# @Author  : 刘登攀
# @Site    : 
# @File    : method.py
# @Software: PyCharm
'''
滑动手机屏幕
'''


# 向上滑动屏幕
def swipe_up(driver, t, n):

    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.75
    y2 = l['height'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向下滑动屏幕
def swipe_down(driver, t, n):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.25
    y2 = l['height'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# '''向左滑动屏幕'''
def swipe_left(driver, t, n):
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.05
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# '''向右滑动屏幕'''
def swipe_right(driver, t, n):
    l = driver.get_window_size()
    x1 = l['width'] * 0.05
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
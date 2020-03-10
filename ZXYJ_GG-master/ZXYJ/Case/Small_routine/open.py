#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18/018 10:05
# @Author  : 刘登攀
# @Site    : 
# @File    : open.py
# @Software: PyCharm
from ZXYJ.Head_Tail.head_up import wechat_up
from ZXYJ.Base.method import swipe_down
import time


def open():
    driver = wechat_up()
    driver.implicitly_wait(10)
    time.sleep(10)
    swipe_down(driver, 500, 1)


if __name__ == '__main__':
    open()

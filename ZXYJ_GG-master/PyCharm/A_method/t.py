#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18/018 17:09
# @Author  : 刘登攀
# @Site    : 
# @File    : t.py
# @Software: PyCharm
import threading
threadlocal = threading.local()


class Test1(object):
    def test1(self):
        print(threading.currentThread())
        print(threadlocal.num)
        print(threading.current_thread().__dict__.get('num'))
        print(threading.currentThread().__dict__.get("num"))


class Test(object):
    def test2(self):
        threadlocal.num = "测试"
        threadlocal.num1 = "测试2"
        # print(threading.currentThread())
        # b = Test1()
        # b.t()
        # print(threadlocal.num1)
        return threadlocal.num1


def tt():
    print(Test().test2())


tt().t()

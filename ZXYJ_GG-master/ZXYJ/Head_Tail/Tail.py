#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10/010 16:09
# @Author  : 刘登攀
# @Site    : 
# @File    : Tail.py
# @Software: PyCharm
from ZXYJ.Base.facility import *
import unittest


# 运行脚本
if __name__ == '__main__':
    for i in path():
        discover = unittest.defaultTestLoader.discover(location()+r'\Case\WeChat_Public', pattern=i)
        runner = unittest.TextTestRunner()
        runner.run(discover)

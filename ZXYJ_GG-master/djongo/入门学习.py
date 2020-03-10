#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14/014 16:13
# @Author  : 刘登攀
# @Site    : 
# @File    : 入门学习.py
# @Software: PyCharm


# 输入 ‘ %s ’是替代符 只有一个值替换的时候不用括号，多个的时候必须要括号，而且要按照顺序来，如果不按顺序来的话会发生什么你可以自己试一下
# 一个值
a = input('输入第一个数：')
print('你输入的第一个数是：%s' % a)
# 两个值--按照顺序
b = input('输入二个数：')
print('你输入的第一个数是：%s,第二个数是：%s' % (a, b))
# 两个值--不按顺序
print('你输入的第一个数是：%s,第二个数是：%s' % (b, a))

# 判断
if a == 1:
    print('恭喜')
else:
    print('错了')
# 多重判断
if a == 1:
    print('恭喜')
elif a == 2 :
    print('再次恭喜')
else:
    print('错了')

# 列表 Python规范：逗号 等号后面需要空格一下
list_a = ['1', '2', '3']
# # 这个和Java一样  list_a[0] = 1
print(list_a[0])

# 字典
list_b = {'a': '1', 'b': '2', 'c': '3'}
print(list_b['b'])

# 循环 循环输出列表(字典一样)
for asd in list_a:
    print(asd)

# 循环输出1-10数(10是0-9 如果你要从1开始就是注释了的那种写法) 如果只填一个数，默认从0开始
# for a in range(1, 11):
for a in range(11):
    print(a)


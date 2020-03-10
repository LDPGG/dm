# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 0004 下午 5:06
# @Author  : 刘登攀阿！！
# @FileName: Slide.py
# @Software: PyCharm
'''
store() # 封装店铺列表填写店铺
route() 封装测试报告保存路径
login() 封装登录方法
swipeUp() 封装手机上滑方法
swipeDown() 封装手机下滑方法
swipLeft() 封装手机左滑方法
swipRight() 封装手机右滑方法
'''


'''--------华-----丽-------的-------分-----割--------线----------------------'''


# 封装店铺列表填写店铺
def store(driver, choice):
    driver.find_element_by_id('s2id_autogen1').send_keys(choice)


'''--------华-----丽-------的-------分-----割--------线----------------------'''


# 封装测试报告保存路径
def route():
    url = 'E:\dm\PyCharm\PyCharm\A_TestReport'
    return url


'''--------华-----丽-------的-------分-----割--------线----------------------'''


# 封装登录
def login(driver, username, passwd):
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('passwd').send_keys(passwd)
    driver.find_element_by_id('submit_login').click()


'''--------华-----丽-------的-------分-----割--------线----------------------'''


# 向上滑动屏幕
def swipe_up(driver, t=500, n=1):

    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.75
    y2 = l['height'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向下滑动屏幕
def swipe_down(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.25
    y2 = l['height'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)


# '''向左滑动屏幕'''
def swipe_left(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.05
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# '''向右滑动屏幕'''
def swipe_right(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.05
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

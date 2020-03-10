# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 0007 上午 11:35
# @Author  : 刘登攀阿！！
# @FileName: Test.py
# @Software: PyCharm
from appium import webdriver
from time import sleep


desired_caps = {
    'platformName': 'Android',
    'deviceName': 'bf18f20a',
    'platformVersion': '4.4.4',
    'appPackage': 'com.tengchi.zxyjsc',
    'appActivity': 'com.tengchi.zxyjsc.module.splash.SplashActivity'
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# sleep(15)
# ac = driver.current_activity
# print(ac)
driver.wait_activity(".module.MainActivity", 30)
driver.find_element_by_id('com.tengchi.zxyjsc:id/tabMeLayout').click()
sleep(10)
# driver.quit()


#   .module.splash.SplashActivity
#   .module.MainActivity
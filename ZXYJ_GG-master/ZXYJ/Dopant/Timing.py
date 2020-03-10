#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28/028 9:18
# @Author  : 刘登攀
# @Site    : 
# @File    : Timing.py
# @Software: PyCharm
import datetime
from ZXYJ.Base.facility import *
from appium import webdriver
import tkinter
'''
钉钉自动打卡
'''


class Ding(object):
    def __init__(self):
        root = tkinter.Tk()
        root.geometry("550x300+800+400")
        root.title('钉钉自动打卡')

        # 标签控件
        # 邮件号
        self.label_n = tkinter.Label(master=root, text='年：')
        self.label_n.grid(row=0, column=0)
        # 间谍号
        self.label_y = tkinter.Label(master=root, text='月：')
        self.label_y.grid(row=0, column=2)
        # 目标群
        self.label_r = tkinter.Label(master=root, text='日：')
        self.label_r.grid(row=0, column=4)
        # 授权码
        self.label_s = tkinter.Label(master=root, text='时：')
        self.label_s.grid(row=1, column=0)
        # 邮件标题
        self.label_f = tkinter.Label(master=root, text='分：')
        self.label_f.grid(row=1, column=2)
        # 邮件标题
        self.label_m = tkinter.Label(master=root, text='秒：')
        self.label_m.grid(row=1, column=4)

        # 输入控件
        # 邮件号
        self.entry_n = tkinter.Entry(master=root, width=10)
        self.entry_n.grid(row=0, column=1)
        # 间谍号
        self.entry_y = tkinter.Entry(master=root, width=10)
        self.entry_y.grid(row=0, column=3)
        # 目标群
        self.entry_r = tkinter.Entry(master=root, width=10)
        self.entry_r.grid(row=0, column=5)
        # 授权码
        self.entry_s = tkinter.Entry(master=root, width=10)
        self.entry_s.grid(row=1, column=1)
        # 邮件标题
        self.entry_f = tkinter.Entry(master=root, width=10)
        self.entry_f.grid(row=1, column=3)
        # 邮件内容
        self.entry_m = tkinter.Entry(master=root, width=10)
        self.entry_m.grid(row=1, column=5)
        # 按钮控件
        # 提交信息按钮
        self.button_tj = tkinter.Button(master=root, text='运  行', command=self.app_time, width=15, height=3)
        self.button_tj.grid(row=2, column=5)
        # 停止按钮
        self.button_tz = tkinter.Button(master=root, text='停  止', command=root.quit, width=15, height=3)
        self.button_tz.grid(row=3, column=5)
        # 清空内容
        self.button_tz = tkinter.Button(master=root, text='清  空', command=self.delete, width=15, height=3)
        self.button_tz.grid(row=4, column=5)
        # # 列表框控
        self.listbox = tkinter.Listbox(master=root, width=55, height=10)
        self.listbox.grid(row=2, column=0, rowspan=3, columnspan=4)
        # 生成界面
        root.mainloop()

    # 清空控件内容
    def delete(self):
        self.entry_n.delete(0, 'end')
        self.entry_y.delete(0, 'end')
        self.entry_r.delete(0, 'end')
        self.entry_s.delete(0, 'end')
        self.entry_f.delete(0, 'end')
        self.entry_m.delete(0, 'end')

    # 清空输入框内容
    def delete_box(self):
        self.listbox.delete(0, 'end')

    def app_time(self):
        # 获取控件时间
        n = self.entry_n.get()
        y = self.entry_y.get()
        r = self.entry_r.get()
        s = self.entry_s.get()
        f = self.entry_f.get()
        m = self.entry_m.get()
        # 定时时间
        timing = datetime.datetime(int(n), int(y), int(r), int(s), int(f), int(m))
        while True:
            # 获取当前时间
            now_time = datetime.datetime.now()
            self.listbox.insert('end', '当前时间为：%s' % now_time)
            self.listbox.see('end')
            self.listbox.update()
            if timing < now_time < (timing+datetime.timedelta(minutes=1)):
                desired_caps = {
                    'platformName': 'Android',
                    'deviceName': devices_t(),
                    'platformVersion': version_t(),
                    'appPackage': 'com.alibaba.android.rimet',
                    'appActivity': 'com.alibaba.android.rimet.biz.SplashActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True
                }
                webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                self.listbox.insert('end', '打卡成功')
                self.listbox.see('end')
                self.listbox.update()
                break
            time.sleep(30)


if __name__ == '__main__':
    Ding().app_time()


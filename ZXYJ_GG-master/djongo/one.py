#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/3/003 14:53
# @Author  : 刘登攀
# @Site    : 
# @File    : one.py
# @Software: PyCharm
# https://kuaiyinshi.com/hot/video/?source=kuai-shou&page=1&st=week
# https://kuaiyinshi.com/hot/video/?source=huo-shan &page=1&st=week
# https://kuaiyinshi.com/hot/video/?source=mei-pai  &page=1&st=week
# https://kuaiyinshi.com/hot/video/?source=dou-yin  &page=1&st=week
from bs4 import BeautifulSoup
import requests
import re
from hashlib import md5
import win32api, win32con
import time
from selenium import webdriver
'''
阿胖：爬取网站视频（美拍，快手，抖音，火山）
'''


# 爬取当月最火视频
class Reptile(object):
    # 获取页面源码
    def __init__(self, url):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = url
        self.driver.get(self.url)
        # 全局隐式等待30秒
        self.driver.implicitly_wait(30)
        time.sleep(6)
        # # 控制屏幕滑动，获取更多群员信息
        for ai in range(20):
            if ai <= 20:
                self.driver.execute_script("window.scrollTo(0,50000)")
                ai += 1
                time.sleep(1)
        # 获取源码
        # time.sleep(5)
        self.res = self.driver.page_source
        # 关闭浏览器
        self.driver.quit()
        # 将源代码存入txt文本
        with open(r'html.txt', 'w', encoding='utf-8') as f:
            f.write(self.res)
        f.close()
        # 读取txt文本
        with open(r'html.txt', 'r', encoding='utf-8') as f:
            self.res = f.read()

    # 抖音
    def douyin(self):
        # request = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(self.res, features="html.parser")
        all_soup = soup.find_all(class_='col-md-3')

        # 获取视频标题与链接
        url = re.findall(r'href=\"(.*?)\"', '%s' % all_soup)
        alt = re.findall(r'list-item-desc">(.*?)</p>', '%s' % all_soup)
        true_href = []
        true_href.append(url)
        for i in range(len(url)):
            # print(alt[i], i+1)
            # 通过假视频链接拼接真视频链接
            true_url = re.findall(r'/\?(.*?)&', '%s' % true_href[0][i])
            url = 'https://api.amemv.com/aweme/v1/playwm/?%s&line=0&ratio=720p&' \
                  'media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0' % true_url[0]
            response = requests.get(url, headers=self.headers)
            data = response.content
            file_path = 'E:\视频\抖音\{}.{}'.format(i+1, 'mp4')
            with open(file_path, 'wb')as f:
                f.write(data)
                f.close()
            with open(r'dy.txt', 'a', encoding='utf-8') as h:
                h.write(alt[i]+'\n')
            h.close()

    # 快手
    def kuaishou(self):
        soup = BeautifulSoup(self.res, features="html.parser")
        all_soup = soup.find_all(class_='col-md-3')
        # 获取视频标题与链接
        url_one = re.findall(r'/\?(.*?)&', '%s' % all_soup)
        url_two = re.findall(r'c/(.*?)_', '%s' % all_soup)
        url_three = re.findall(r'_b_(.*?)&', '%s' % all_soup)
        alt = re.findall(r'list-item-desc">(.*?)</p>', '%s' % all_soup)
        for i in range(len(url_one)):
            url_t = 'https://jsmov2.a.yximgs.com/upic/%s_b_%s.mp4' % (url_two[i], url_three[i])
            print(url_t)
            response = requests.get(url_t, headers=self.headers)
            data = response.content
            file_path = 'E:\视频\快手\{}.{}'.format(i+1, 'mp4')
            with open(file_path, 'wb')as f:
                f.write(data)
                f.close()
            with open(r'dy.txt', 'a', encoding='utf-8') as h:
                h.write(alt[i]+'\n')
            h.close()
    # 火山
    def huosan(self):
        soup = BeautifulSoup(self.res, features="html.parser")
        all_soup = soup.find_all(class_='col-md-3')
        # print(all_soup)
        fll = re.findall('/\?(.*?)&', '%s' % all_soup)
        for i in range(len(fll)):
            h_url = 'https://api.huoshan.com/hotsoon/item/video/_playback/' \
                    '?%s&line=0&app_id=1112&vquality=normal&quality=720p' % fll[i]
            response = requests.get(h_url, headers=self.headers)
            data = response.content
            file_path = 'E:\视频\{}.{}'.format(md5(data).hexdigest(), 'mp4')
            with open(file_path, 'wb')as f:
                f.write(data)
                f.close()

    # 美拍
    def meipai(self):
        soup = BeautifulSoup(self.res, features="html.parser")
        all_soup = soup.find_all(class_='col-md-3')
        # print(all_soup)
        fll = re.findall('video_id=(.*?)&', '%s' % all_soup)
        for i in range(len(fll)):
            h_url = 'https://mvvideo10.meitudata.com/%s.mp4' % fll[i]
            response = requests.get(h_url, headers=self.headers)
            data = response.content
            file_path = 'E:\视频\{}.{}'.format(md5(data).hexdigest(), 'mp4')
            with open(file_path, 'wb')as f:
                f.write(data)
                f.close()


if __name__ == '__main__':
    print('仅支持：快手，火山，抖音，美拍')
    site = input('请输入您的理想平台：')
    if '快手' in site:
        url = 'https://kuaiyinshi.com/hot/video/?source=kuai-shou&page=1&st=month'
        Reptile(url=url).kuaishou()
    elif '火山' in site:
        url = 'https://kuaiyinshi.com/hot/video/?source=huo-shan &page=1&st=month'
        Reptile(url=url).huosan()
    elif '美拍' in site:
        url = 'https://kuaiyinshi.com/hot/video/?source=mei-pai  &page=1&st=month'
        Reptile(url=url).douyin()
    elif '抖音' in site:
        url = 'https://kuaiyinshi.com/hot/video/?source=dou-yin&page=1&st=month'
        Reptile(url=url).douyin()
    else:
        win32api.MessageBox(0, "看提示输入，电脑都能遭你气死", "真蠢啊你", win32con.MB_ICONASTERISK)



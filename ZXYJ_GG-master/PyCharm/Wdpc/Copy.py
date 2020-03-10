# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 0012 下午 5:41
# @Author  : 刘登攀阿！！
# @FileName: Copy.py

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os

'''
爬取图片保存至本地
'''
if __name__ == '__main__':
    # 创建文件夹
    if 'image' not in os.listdir():
        os.makedirs('image')
    # 设置存放图片路径的容器
    list_url = []
    # 页数
    for nnm in range(1, 3):
        if nnm == 1:
            # 设置网页
            url = 'http://cd.58.com/zufang/0/j1'
        else:
            # 设置网页（多页情况下）
            url = 'http://www.shuaia.net/dongman/index_%s.html'% nnm
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }
        # 请求数据
        rtt = requests.get(url=url, headers=headers)
        # 设置编码格式
        rtt.encoding = 'UTF-8'
        #print(rtt.text)
        # 遍历文档树
        Soup = BeautifulSoup(rtt.text, 'lxml')
        # 搜索文档树
        fall_url = Soup.find_all(class_='item-img-box')
        for each in fall_url:
            # 这里改一下标签
            list_url.append(each.a.img.get('alt')+"="+each.a.get('href'))
        # 检测你是否拿到网页源码
        # print(list_url)
    print('数据采集完毕')

    for each_img in list_url:
        # 分割字符
        img_info = each_img.split("=")
        # 取地址
        target_url = img_info[1]
        # 设置保存图片名称格式
        fileName = img_info[0]+'.jpg'
        print('下载：'+fileName)
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }
        # 请求数据
        rtt = requests.get(url=target_url, headers=headers)
        # 设置编码格式（看网页编码格式改不改）
        rtt.encoding = 'UTF-8'
        html = rtt.text
        # 遍历文档树
        Soup_1 = BeautifulSoup(html, 'lxml')
        # 搜索文档树（看div里class标签改）
        img_url = fall_url = Soup_1.find_all('div', class_='wr-single-content-list')
        bf_1 = BeautifulSoup(str(img_url), 'lxml')
        try:
            # 这里改一下标签
            img_url = "http://www.shuaia.net/"+bf_1.div.img.get('src')
            urlretrieve(url=img_url, filename='image/'+fileName)
        except:
            print('你代码错了')
            break
    print('下载完成')

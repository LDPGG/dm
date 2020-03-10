# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 0012 下午 5:41
# @Author  : 攀哥哥阿！！
# @FileName: Copy.py

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
'''
进阶爬取图片保存至本地
'''

if __name__ == '__main__':
    # 创建文件夹存放图片
    if 'image' not in os.listdir():
        os.makedirs('image')
    list_url = []

    # 设置网页（我爬的糗事百科）
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=python&ct=201326592&lm=-1&v=flip'
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    # 请求数据
    rtt = requests.get(url=url, headers=headers)
    # 设置编码格式(自己查看网页格式。基本就GBK或者UTF-8)
    rtt.encoding = 'UTF-8'
    # print(rtt.text)
    # 遍历文档树
    Soup = BeautifulSoup(rtt.text, 'lxml')
    # 搜索文档树
    fall_url = Soup.find_all(class_='imglist')
    for each in fall_url:
        # 获取详细大图的跳转路径
        list_url.append("http://image.baidu.com/"+each.a.list.get('href'))
        # 查看获取到的信息
    print(list_url)
    # print('数据采集完毕')

    for each_img in list_url:
        # 分割字符
        img_info = each_img.split("=")
        # 取地址
        target_url = img_info[1]
        # 设置保存图片名称格式
        fileName = img_info[0]+'.jpeg'
        print('下载：'+fileName)
        # 设置请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }
        # 请求数据
        rtt = requests.get(url=target_url, headers=headers)
        # 设置编码格式
        rtt.encoding = 'GBK'
        html = rtt.text
        # 遍历文档树
        Soup_1 = BeautifulSoup(html, 'lxml')
        # 搜索文档树
        img_url = fall_url = Soup_1.find_all('div', class_='_2yFK- IEpfq')
        bf_1 = BeautifulSoup(str(img_url), 'lxml')
        try:
            # 获取详细大图的路径(如果前缀被隐藏，记得自己要加上去)
            img_url = bf_1.img.get('srcset')
            urlretrieve(url=img_url, filename='image/'+fileName)
        except:
            print('没找到图片')
            break
    print('下载完成')

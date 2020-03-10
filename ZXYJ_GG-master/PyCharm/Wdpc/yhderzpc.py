
# @Time    : 2018/6/12 0012 上午 11:30
# @Author  : 刘登攀阿！！
# @FileName: yhderzpc.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re
import os


def get_ima(url):
    headers = {  # 这就是欺骗网页的一个方法
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)  # 获取网页
    # 因为我是小白用的还是3.6Python，这里研究了半天才明白，Python3.x以上因为把好几个urllib包合并了，所有不能直接urllib.urlopen()
    response = urllib.request.urlopen(request)  # 获取服务器响应
    get_img = response.read()  # 读取图片
    return get_img


def get_imas(html):
    print('图片正在准备下载，请稍等。。。。。')
    # 正则是硬伤
    rege = 'http://[\S]*\.jpg'  # 你要爬取的图片的地址格式（正则，百度就行了）
#   print(rege)  测试去的没有任何意义
    pattern = re.compile(rege)  # 将地址编译成字节
    get_img = re.findall(pattern, repr(html))  # 用findall查询出所有与字节匹配的地址  用repr用来转换表达式类型字符串
    num = 0

    #  我的想法是在这里加一个新的for循环，但是我试了，行不通。
    path = 'D:\\tupian\\tupian1'
    if not os.path.isdir(path):
        os.makedirs(path)
    path = path+'\\'  # 保存在test路径下
    for aa in get_img:
        urllib.request.urlretrieve(aa, '%s%s.jpg' % (path, num))
        num += 1
        print('正在下载第%s张图片。。。请稍后' % num)
    return get_img

#  for x in range(21):  # 我本来是想爬糗事百科的，但是我技术太菜，它的图片路径我不会爬，就改成论坛了
#    x += 1
url = 'http://tieba.baidu.com/p/3108805355?pn=1'  # 这里是你要爬的网址路径
html = get_ima(url)  # 将网址传到你上面的方法中
get_imas(html)


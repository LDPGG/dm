#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20/020 10:29
# @Author  : 刘登攀
# @Site    : 
# @File    : contrast.py
# @Software: PyCharm
import requests
import re
from ZXYJ.Dopant.buy import Buy
import time

'''
返利测试
'''


class Contrast(object):
    def __init__(self):
        self.session = requests.session()
        self.phone = '15575555555'
        # 登录
        post_url = 'http://39.108.195.48:8080/flyweb/user/login'
        post_login = {'username': 'admin',
                      'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
        self.session.post(post_url, data=post_login)

    def check(self):
        # 查找订单
        indent_url = 'http://39.108.195.48:8080/flyweb/order/queryOrderList?pager.offset=0&pager.size=10'
        indent_post = {'orderProfitStatus': '99',
                       'orderprofit': '1',
                       'memberPhone': self.phone,
                       'falg': '0',
                       'orderStatus': '99',
                       'payType': '99',
                       'isStore': '0'}
        indent_order_code = self.session.post(indent_url, data=indent_post).json()
        # print(indent_order_code)
        # 订单号
        order_code = indent_order_code['data']['datas'][0]['orderCode']

        #查看订单收益收益
        earnings_url = 'http://39.108.195.48:8080/flyweb/order/queryOrderProfitList?pager.offset=0&pager.size=10'
        earnings_post = {'orderCode': order_code}
        earnings = self.session.post(earnings_url, data=earnings_post).json()
        # 下级账号
        c = re.findall('\'phone\': \'(.*?)\', \'nickName\'', '%s' % earnings)
        # 分销金额
        b = re.findall('\'freezeProfitMoney\': (.*?), \'freezeSumMoney\'', '%s' % earnings)

        # 设置一个变量计数
        grade = 1
        for ii in range(len(b)):
            tt = b[ii]
            tt = int(tt)/100
            print('%s级分销利润：%s' % (grade, tt))
            grade = grade+1

        # 存放上级当前的利润
        present = []
        present_1 = []
        # 计算当前上级的旧收益
        for i in range(len(c)):
            phone = c[i]
            superior_url = 'http://39.108.195.48:8080/flyweb/member/queryMemberList?pager.offset=0&pager.size=10'
            superior_post = {'keys': phone,
                             'grade': '99'}
            superior = self.session.post(superior_url, data=superior_post).json()
            # 存放上级当前利润
            present.append(superior['data']['datas'][0]['freezeSumMoney']/100)
        print('当前的上级当前收益：%s\n' % present)

        # 调用购买方法
        Buy().gm()
        print('请等待。。。\n')
        # 等待订单计算完成
        time.sleep(7)

        # 计算当前上级的新收益
        for i in range(len(c)):
            phone_1 = c[i]
            superior_url_1 = 'http://39.108.195.48:8080/flyweb/member/queryMemberList?pager.offset=0&pager.size=10'
            superior_post_1 = {'keys': phone_1,
                               'grade': '99'}
            superior = self.session.post(superior_url_1, data=superior_post_1).json()
            # 存放上级当前利润
            present_1.append(superior['data']['datas'][0]['freezeSumMoney']/100)
        print('新的上级当前收益：%s\n' % present_1)

        for iii in range(len(present)):
            new_one = present_1[iii]-present[iii]
            new_one_1 = round(new_one, 2)
            print('收益差距：%s' % new_one_1)


if __name__ == '__main__':
    Contrast().check()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21/021 13:52
# @Author  : 刘登攀
# @Site    : 
# @File    : synchronization.py
# @Software: PyCharm
import requests


session = requests.session()


def synchronization():
    login_url = 'http://g.zxyj.com/flyweb/user/login'
    login_data = {'username': '刘登攀',
                  'passwd': 'c8837b23ff8aaa8a2dde915473ce0991'}
    session.post(login_url, login_data)

    query_order_list_url = 'http://g.zxyj.com/flyweb/order/queryOrderList?pager.offset=0&pager.size=200'
    query_order_list__data = {'orderProfitStatus': '99',
                           'orderprofit': '1',
                           'falg': '0',
                           'orderStatus': '2',
                           'payType': '99',
                           'isStore': '0',
                           'orderType': '5'}
    query_order_list = session.post(query_order_list_url, query_order_list__data).json()
    for i in range(0, 200):
        pay_date = query_order_list['data']['datas'][i]['payDate']
        order_code = query_order_list['data']['datas'][i]['orderCode']
        if pay_date == '2019-05-21 09:46:34':
            shop_url = 'http://g.zxyj.com/flyweb/order/ship'
            ship_data = {'orderCode': order_code,
                         'expressName': '申通快递',
                         'expressNo': 'STO',
                         'expressCode': '111111',
                         'sellerRemark': ''
                         }
            ship = session.post(shop_url, ship_data).json()
            print(order_code, ship['message'])
        else:
            print('没有找到订单')


if __name__ == '__main__':
    synchronization()
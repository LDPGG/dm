#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/30/030 17:56
# @Author  : 刘登攀
# @Site    : 
# @File    : ttt.py
# @Software: PyCharm
import requests
'''
已收货订单退货退款
'''


def buy(phone):
    session = requests.Session()
    # 登录
    login_url = 'http://testapi.zxyjsc.com:8090/flyweb/user/login'
    login_data = {'username': '刘登攀', 'passwd': 'c8837b23ff8aaa8a2dde915473ce0991'}
    session.post(login_url, data=login_data)

    member_url = 'http://testapi.zxyjsc.com:8090/flyweb/member/queryMemberList?pager.offset=0&pager.size=10'
    member_data = {'keys': phone,
                   'grade': '99',
                   'registerType': '99'
                   }
    member = session.post(member_url, member_data).json()
    memberId = member['data']['datas'][0]['memberId']

    Coupon_url = 'http://testapi.zxyjsc.com:8090/flyweb/member/memberCouponList?pager.offset=0&pager.size=10'
    Coupon_data = {'memberId': memberId,
                   'status': '99',
                   'couponType': '99',
                   'type': '99',
                   'title': '预售抵扣现金'
                   }
    Coupon = session.post(Coupon_url, Coupon_data).json()
    couponId = Coupon['data']['datas'][0]['couponId']
    sum = Coupon['data']['datas']
    print(len(sum))

    if len(sum) == 1:
        # print('一张')
        url = 'http://testapi.zxyjsc.com:8090/flyweb/product/updateCouponStatus'
        data = {'memberId': memberId, 'couponId': couponId}
        a = session.post(url, data).json()
        print(phone, a['message'])
    elif len(sum) == 2:
        print('两张优惠券，跳过')
    else:
        print('超过两张或者没找到优惠券')


if __name__ == '__main__':
    phone = '15396261141'
    buy(phone)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13/013 9:44
# @Author  : 刘登攀
# @Site    : 
# @File    : buy.py
# @Software: PyCharm
import requests
from random import Random
'''
购买
'''


class Buy(object):
    def __init__(self):
        # 读取记事本
        f = r'C:\Users\Administrator\Desktop\ppp.txt'
        self.pon = open(f, 'r').readlines()

        # 普通产品
        self.sku_id = '040006b0daec44dea4043dcda9da0823'

        # 开店礼包
        # self.sku_id = 'ad4cf9836e4d4ba7974e346dd4bcdea2'

        # 随机生成token
        length_r = 32
        self.token = ''
        chars = '01'
        length = len(chars) - 1
        random = Random()
        for i in range(length_r):
            self.token += chars[random.randint(0, length)]

    # 购买产品
    def gm(self):
        for phones in self.pon:
            phone = phones.strip()
            session = requests.Session()
            # 登陆
            url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"
            test_login_data = {'username': '17897897839', "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
            login = session.post(url=url_login_test, data=test_login_data).json()
            member_id = login['data']['memberId']

            # 获取收货地址
            url_get_address = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
            get_address = session.get(url=url_get_address).json()
            if get_address['data']['datas']:
                # 生成订单
                url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"

                # 店主礼包
                # add_data = '{"orderFrom":1,"couponId":"","orderType":4,"remark":"","products":[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' % (skuId, quantity, addressId)
                # 普通产品
                address_id = get_address['data']['datas'][0]['addressId']
                add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":"1"}],"addressId":"%s"}' % (self.sku_id, address_id)
                pay_order = session.post(url_add, data=add_data).json()
                print(pay_order['message'])
                # # 获取待支付订单列表
                # url_get_order = "http://39.108.195.82:8080/flyapi/popupOrder/getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
                # session.get(url_get_order, data='').json()
                # # 设置支付密码
                # url_set_pwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
                # set_pwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
                # session.post(url_set_pwd, data=set_pwd_data)
                #
                # # 验证支付密码
                # url_give_pwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
                # session.get(url_give_pwd, data='').json()

                # 支付订单
                url_pay_pwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
                pay_pwd_data = {'orderCode': pay_order['data']['orderCode'], "password": 'e10adc3949ba59abbe56e057f20f883e'}
                pay_pwd = session.post(url_pay_pwd, data=pay_pwd_data).json()
                print(pay_pwd['message'])
            else:
                # 添加新收货地址
                url_address_test = "http://39.108.195.82:8080/flyapi/address/add?version=1.0"
                test_address_data = {'phone': phone,
                                     'provinceId': "130000", 'cityId': '130300',
                                     'districtId': '130303', 'districtName': '东河区',
                                     'cityName': '包头市', 'provinceName': '内蒙古自治区',
                                     'detail': '不想写', 'isDefault': '1',
                                     'contact': 'weiwen', 'memberId': member_id}
                session.post(url_address_test, data=test_address_data)
                Buy().gm()


if __name__ == '__main__':
    Buy().gm()

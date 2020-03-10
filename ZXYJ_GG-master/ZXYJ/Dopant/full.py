#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11/011 9:50
# @Author  : 刘登攀
# @Site    : 
# @File    : full.py
# @Software: PyCharm
import requests
from random import Random
import time
'''
注册-加钱
'''


def add_user(up_phone, phone):
    session = requests.session()
    # 随机生成token
    length_r = 32
    token = ''
    chars = '01'
    length = len(chars) - 1
    random = Random()
    for i in range(length_r):
        token += chars[random.randint(0, length)]
    url = 'http://39.108.195.82/flyapi/user/add'
    data = {'invitationCode': up_phone,
            'phone': phone,
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'checkNumber': '20160920',
            'token': token,
            'registerType': '1',
            'version': '1.0',
            'terminal': '3'
            }
    a = session.post(url, data).json()
    print(a)
    time.sleep(4)

    url_login_test = "http://39.108.195.48:8080/flyweb/user/login"
    test_login_data = {'username': 'admin', "passwd": 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(url_login_test, data=test_login_data)

    url_query = 'http://39.108.195.48:8080/flyweb/member/queryMemberListForUpdate?pager.offset=0&pager.size=10'
    test_query = {"keys": phone}
    query = session.post(url_query, data=test_query).json()
    member_id = query['data']['datas'][0]['memberId']

    url_member_money = 'http://39.108.195.48:8080/flyweb/member/addMemberMoney'
    add_member_id_data = {'memberId': member_id,
                          'money': '999999',
                          'type': '6',
                          'changeReason': '测试',
                          'phone': phone,
                          'token': token}
    session.post(url_member_money, data=add_member_id_data)

    url_get_change = 'http://39.108.195.48:8080/flyweb/member/changeExamineList?pager.offset=0&pager.size=10'
    test_get_change = {'userPhone': phone, 'type': '99'}
    get_change_id = session.post(url_get_change, data=test_get_change).json()
    # print(get_change_id)
    get_change_id = get_change_id['data']['datas'][0]['changeId']

    url_update_money = 'http://39.108.195.48:8080/flyweb/member/updateChangeExamine'
    test_url_update_money = {'changeId': get_change_id, "status": '1'}
    update_money = session.post(url_update_money, data=test_url_update_money).json()
    print(phone, update_money['message'])


if __name__ == '__main__':
    up_phone = '18166220017'
    phone = '18166220018'
    add_user(up_phone, phone)
    # # 注册
    # def zc(self):
    #     shangji = input('上级：')
    #     for nowPhone in self.pon:
    #         phone = nowPhone.strip()
    #         session = requests.Session()
    #         # 认证上级
    #         url_superior = 'http://39.108.195.82:8080/flyapi/user/getMemberInfoByInviteCode?inviteCode=%s&version=1.0&terminal=1' % shangji
    #         r = session.get(url=url_superior).json()
    #         code = r['data']['inviteCode']
    #
    #         # 随机生成token
    #         length_r = 32
    #         token = ''
    #         chars = '01'
    #         length = len(chars) - 1
    #         random = Random()
    #         for i in range(length_r):
    #             token += chars[random.randint(0, length)]
    #
    #         # 注册
    #         url_zc = 'http://39.108.195.82:8080/flyapi/user/add?version=1.0&terminal=1'
    #         data_zc = {'password': 'e10adc3949ba59abbe56e057f20f883e',
    #                    'checkNumber': '20160920',
    #                    'phone': phone,
    #                    'invitationCode': code,
    #                    'token': token
    #                    }
    #         t = session.post(url=url_zc, data=data_zc).json()
    #         print(t)
    #         print(t['message'])
    #
    # # 加钱
    # def jq(self):
    #     session = requests.Session()
    #     # 读取记事本
    #     f = r'C:\Users\Administrator\Desktop\ppp.txt'
    #     pon = open(f, 'r').readlines()
    #
    #     url_login_test = "http://39.108.195.48:8080/flyweb/user/login"
    #     test_login_data = {'username': 'admin', "passwd": 'e10adc3949ba59abbe56e057f20f883e'}
    #     session.post(url_login_test, data=test_login_data)
    #
    #     for nowPhone in pon:
    #         phone = nowPhone.replace('\n', '')
    #         url_query = 'http://39.108.195.48:8080/flyweb/member/queryMemberListForUpdate?pager.offset=0&pager.size=10'
    #         test_query = {"keys": phone}
    #         query = session.post(url_query, data=test_query).json()
    #         member_id = query['data']['datas'][0]['memberId']
    #
    #         # 随机生成token
    #         length_r = 32
    #         token = ''
    #         chars = '01'
    #         length = len(chars) - 1
    #         random = Random()
    #         for i in range(length_r):
    #             token += chars[random.randint(0, length)]
    #
    #         url_member_money = 'http://39.108.195.48:8080/flyweb/member/addMemberMoney'
    #         add_member_id_data = {'memberId': member_id,
    #                               'money': '999999',
    #                               'type': '6',
    #                               'changeReason': '测试',
    #                               'phone': phone,
    #                               'token': token}
    #         session.post(url_member_money, data=add_member_id_data)
    #
    #         url_get_change = 'http://39.108.195.48:8080/flyweb/member/changeExamineList?pager.offset=0&pager.size=10'
    #         test_get_change = {'userPhone': phone, 'type': '99'}
    #         get_change_id = session.post(url_get_change, data=test_get_change).json()
    #         # print(get_change_id)
    #         get_change_id = get_change_id['data']['datas'][0]['changeId']
    #
    #         url_update_money = 'http://39.108.195.48:8080/flyweb/member/updateChangeExamine'
    #         test_url_update_money = {'changeId': get_change_id, "status": '1'}
    #         update_money = session.post(url_update_money, data=test_url_update_money).json()
    #         print(phone, update_money['message'])
    #
    # # 购买产品
    # def gm(self):
    #     session = requests.Session()
    #     for phones in self.pon:
    #
    #         phone = phones.strip()
    #         # 登陆
    #         url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"
    #         print(phone)
    #         test_login_data = {'username': phone, "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
    #         login = session.post(url_login_test, data=test_login_data).json()
    #         member_id = login['data']['memberId']
    #
    #         # 获取收货地址
    #         url_get_address = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
    #         get_address = session.get(url_get_address, data='').json()
    #         if get_address['data']['datas']:
    #             # 生成订单
    #             url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"
    #
    #             address_id = get_address['data']['datas'][0]['addressId']
    #             # 店主礼包
    #             # add_data = '{"orderFrom":1,"couponId":"","orderType":4,"remark":"","products":[{"skuId":"%s","quantity":"1"}],"addressId":"%s"}' % (self.sku_id, address_id)
    #             # 普通产品
    #             add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":"1"}],"addressId":"%s"}' % (self.sku_id, address_id)
    #             pay_order = session.post(url_add, data=add_data).json()
    #             print(pay_order['message'])
    #             # 获取待支付订单列表
    #             url_get_order = "http://39.108.195.82:8080/flyapi/popupOrder/getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
    #             session.get(url_get_order, data='').json()
    #             # 设置支付密码
    #             url_set_pwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
    #             set_pwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
    #             session.post(url_set_pwd, data=set_pwd_data)
    #
    #             # 验证支付密码
    #             url_give_pwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
    #             session.get(url_give_pwd, data='').json()
    #
    #             # # 支付订单
    #             # url_pay_pwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
    #             # pay_pwd_data = {'orderCode': pay_order['data']['orderCode'], "password": 'e10adc3949ba59abbe56e057f20f883e'}
    #             # pay_pwd = session.post(url_pay_pwd, data=pay_pwd_data).json()
    #             # print(pay_pwd['message'])
    #         else:
    #             # 添加新收货地址
    #             url_address_test = "http://39.108.195.82:8080/flyapi/address/add?version=1.0"
    #             test_address_data = {'phone': phone,
    #                                  'provinceId': "130000", 'cityId': '130300',
    #                                  'districtId': '130303', 'districtName': '白云区',
    #                                  'cityName': '广州市', 'provinceName': '广东省',
    #                                  'detail': '不想写', 'isDefault': '1',
    #                                  'contact': 'weiwen', 'memberId': member_id}
    #             session.post(url_address_test, data=test_address_data)
    #             Full().call_back(phone)
    #
    # # 回调购买方法
    # def call_back(self, phone):
    #     session = requests.Session()
    #     url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"
    #
    #     test_login_data = {'username': phone, "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
    #     login = session.post(url_login_test, data=test_login_data).json()
    #     member_id = login['data']['memberId']
    #
    #     # 获取收货地址
    #     url_get_address = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
    #     get_address = session.get(url_get_address, data='').json()
    #     # 生成订单
    #     url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"
    #
    #     address_id = get_address['data']['datas'][0]['addressId']
    #     # 店主礼包
    #     # add_data = '{"orderFrom":1,"couponId":"","orderType":4,"remark":"","products":[{"skuId":"%s","quantity":"1"}],"addressId":"%s"}' % (self.sku_id, address_id)
    #     # 普通产品
    #     add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":"1"}],"addressId":"%s"}' % (self.sku_id, address_id)
    #     pay_order = session.post(url_add, data=add_data).json()
    #     print(pay_order['message'])
    #     # 获取待支付订单列表
    #     url_get_order = "http://39.108.195.82:8080/flyapi/popupOrder/getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
    #     session.get(url_get_order, data='').json()
    #     # 设置支付密码
    #     url_set_pwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
    #     set_pwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
    #     session.post(url_set_pwd, data=set_pwd_data)
    #
    #     # 验证支付密码
    #     url_give_pwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
    #     session.get(url_give_pwd, data='').json()
    #
    #     # 支付订单
    #     url_pay_pwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
    #     pay_pwd_data = {'orderCode': pay_order['data']['orderCode'], "password": 'e10adc3949ba59abbe56e057f20f883e'}
    #     pay_pwd = session.post(url_pay_pwd, data=pay_pwd_data).json()
    #     print(pay_pwd['message'])


# if __name__ == '__main__':
#     f = Full()
#     f.zc()
#     f.jq()
#     # f.gm()

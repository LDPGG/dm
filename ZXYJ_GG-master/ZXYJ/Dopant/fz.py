#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5/005 11:55
# @Author  : 刘登攀
# @Site    : 
# @File    : fz.py
# @Software: PyCharm
import requests
from random import Random
import json


def fz():
    # 登陆
    session = requests.Session()
    url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"
    test_login_data = {'username': '15386174586', "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
    session.post(url=url_login_test, data=test_login_data).json()
    # 获取addressId
    url_id = 'http://39.108.195.82:8080/flyapi/address/getdefault?version=1.0&terminal=1'
    id = session.get(url_id).json()
    addressId = id['data']['addressId']
    # 随机生成token
    length_r = 32
    token = ''
    chars = '01'
    length = len(chars) - 1
    random = Random()
    for i in range(length_r):
        token += chars[random.randint(0, length)]
    # url_gm_data = {"addressId": '%s' % addressId, "couponId": "", "products": [{"quantity": '2', "skuId": skuid_3}], "remark": "", "orderFrom": '1'}
    url_gm = 'http://39.108.195.82:8080/flyapi/order/add?token=%s&version=1.0&terminal=1' % token
    # TCL水壶
    skuid_1 = '511fdab5534d485cba396a2d483db608'
    # TCL料理机
    skuid_2 = '22e616cab17d4c1e9f7cddf4d428e2cc'
    # 兮雅包包
    skuid_3 = '411d50ea287349fcb217cecbe2bc2684'
    # 兮雅小包
    skuid_4 = '2a7cd80f9148430991b3bbf573bd152f'
    # 分账产品
    skuid_5 = 'bda089bc745040c091b8bad87101c129'
    # 慕斯内衣
    skuid_6 = '065b2283e6f44522a6998941191f9a67'
    # 多产品下单
    url_gm_data = {"addressId": '%s' % addressId, "couponId": "", "products": [{"quantity": '1', "skuId": skuid_4},
                                                                               {"quantity": '1', "skuId": skuid_5},
                                                                               {"quantity": '1', "skuId": skuid_6}], "remark": "", "orderFrom": '1'}

    # 查看购物车产品
    url_gw_c = 'http://39.108.195.82:8080/flyapi/cart/member/list?version=1.0&terminal=1'
    gw_c = session.get(url_gw_c).json()
    # gw_c_1 = gw_c['data'][0]['skuProductList'][0]['skuName']
    gwc = int(len(gw_c['data']))
    i = 0
    while i < gwc:
        gw_c_1 = gw_c['data'][i]['skuProductList'][0]['skuName']
        gw_c_2 = gw_c['data'][i]['skuProductList'][0]['quantity']
        print('产品名称：%s\t产品数量：%s' % (gw_c_1, gw_c_2))
        i += 1

    # 提交订单
    headers = {'content-type': "application/json"}
    gm = session.post(url_gm, data=json.dumps(url_gm_data), headers=headers).json()
    print(gm['message'])


if __name__ == '__main__':
    fz()

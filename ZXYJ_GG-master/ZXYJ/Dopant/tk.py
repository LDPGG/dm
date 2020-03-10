#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/11/011 14:09
# @Author  : 刘登攀
# @Site    : 
# @File    : tk.py
# @Software: PyCharm
import requests
import time

for i in range(0, 17):
    session = requests.session()
    post_url = 'http://39.108.195.48:8080/flyweb/user/login'
    post_login = {'username': 'admin', 'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(post_url, data=post_login)

    jl_url = 'http://39.108.195.48:8080/flyweb/refundorder/queryOrderList?pager.offset=0&pager.size=10'
    jl_post = {'memberPhone': '15386174586', 'orderStatus': '4', 'payType': '99'}
    a = session.post(jl_url, jl_post).json()
    print(a)
    b = a['data']['datas'][0]['payMoney']

    th_url = 'http://39.108.195.48:8080/flyweb/refundorder/saveRefundDapply'
    th_post = {'orderId': a['data']['datas'][0]['orderId'],
               'memberId': 'dba0cee8f0194429ac07c317255181d7',
               'refundReason': '拍错了/信息填写错误',
               'applyRefundMoneyStr': b/100,
               'refundType': '1',
               'orderCode': a['data']['datas'][0]['orderCode'],
               'refundStatus': '7'}
    c = session.post(th_url, th_post).json()
    print(c)

    tt_url = 'http://39.108.195.48:8080/flyweb/refundorder/allowRefundGoods'
    tt_post = {'orderCode': a['data']['datas'][0]['orderCode'],
               'orderId': a['data']['datas'][0]['orderId'],
               'memberId': 'dba0cee8f0194429ac07c317255181d7'}
    d = session.post(tt_url, tt_post).json()
    print(d)

    tp_url = 'http://39.108.195.48:8080/flyweb/refundorder/uploadMsg'
    tp_post = {'orderCode': a['data']['datas'][0]['orderCode'],
               'orderId': a['data']['datas'][0]['orderId'],
               'memberId': 'dba0cee8f0194429ac07c317255181d7',
               'refundGoodsExpressName': '哈哈哈',
               'refundGoodsExpressCode': '213213213'}
    e = session.post(tp_url, tp_post).json()
    print(e)

    pp_url = 'http://39.108.195.48:8080/flyweb/refundorder/sureReceiveGoods'
    pp_post = {'orderCode': a['data']['datas'][0]['orderCode'],
               'orderId': a['data']['datas'][0]['orderId'],
               'memberId': 'dba0cee8f0194429ac07c317255181d7'}
    f = session.post(pp_url, pp_post).json()
    print(f)

    uu_url = 'http://39.108.195.48:8080/flyweb/refundorder/updateMoney'
    uu_post = {'orderCode': a['data']['datas'][0]['orderCode'],
               'orderId': a['data']['datas'][0]['orderId'],
               'memberId': 'dba0cee8f0194429ac07c317255181d7',
               'refundMoneyStr': b/100}
    'orderCode=2151552498850606&orderId=03b617d4a8e847ecb224e6ee01522a7b&memberId=dba0cee8f0194429ac07c317255181d7&dealContent=&refundMoneyStr=0.40&sellerRemark='
    g = session.post(uu_url, uu_post).json()
    print(g)
    i += 1
    time.sleep(1)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30/030 15:40
# @Author  : 刘登攀
# @Site    : 
# @File    : rebate .py
# @Software: PyCharm\
import requests
from random import Random
import json
import time


session = requests.Session()


# 购买下单
def purchase(opemID, skuId):
    # for i in range(10):
        # 登陆  自己修改为自己账户的openId
        login_url = 'http://39.108.195.100:8088/groupApi/wechatLogin'
        login_date = {'openId': opemID[0],
                      'version': '1.0'}
        log = session.post(login_url, login_date).json()
        print(log['message'])

        # 随机生成token
        length_r = 32
        token = ''
        chars = '01'
        length = len(chars) - 1
        random = Random()
        for i in range(length_r):
            token += chars[random.randint(0, length)]

        tj_url = 'http://39.108.195.100:8088/groupApi/order/batchAddOrder?terminal=3&version=1.0&token=%s' % token
        headers = {'content-type': "application/json"}
        tj_data = {"orderType": 0,
                   "orderFrom": 3,
                   "remark": "",
                   "products": [{"phone": "14857477373",
                                 "contact": "就是就是",
                                 "province": "辽宁省",
                                 "city": "丹东市",
                                 "area": "宽甸满族自治县",
                                 "detail": "不到好多活到九十九",
                                 "buyerRemark": "",
                                 "skus": [{"skuId": skuId[0],
                                           "quantity": "1"}]
                                 }]
                   }
        tj = session.put(tj_url, data=json.dumps(tj_data), headers=headers).json()
        print(tj['message'])
        order_code = tj['data'][0]['orderCode']
        print('订单：'+tj['data'][0]['orderCode']+tj['message'])

        zf_url = 'http://39.108.195.100:8088/groupApi/order/payPwd'
        zf_data = {'orderCode': order_code,
                   'password': 'e10adc3949ba59abbe56e057f20f883e',
                   'version': '1.0',
                   'terminal': '4',
                   'payType': '0'}
        tj = session.post(zf_url, zf_data).json()
        print(tj['message'])


# 后台确认收货
def consignment(opemId, phone):
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'ldp001',
                   'password': 'e10adc3949ba59abbe56e057f20f883e'}
    a = session.post(ht_log_url, ht_log_data).json()
    # print(a)

    # 根据手机号搜索后的第一条数据
    phone_url = 'http://39.108.195.82:8080/groupWebApi/order/list/pager?status=2&pageOffset=1&pageSize=10&version=1.0&keys=%s' % phone[0]
    ph = session.get(phone_url).json()
    order_code_1 = ph['data']['datas'][0]['orderCode']

    # 获取全部订单的第一条数据
    # ht_dd_url = 'http://39.108.195.82:8080/groupWebApi/order/list/pager?pageOffset=1&pageSize=10&version=1.0'
    # dd = session.get(ht_dd_url).json()
    # order_code_1 = dd['data']['datas'][0]['orderCode']
    # print(orderCode_1)

    ht_fh_url = 'http://39.108.195.82:8080/groupWebApi/order/ship?expressName=&expressCode=11111&expressNo=JD&orderCode=%s&version=1.0' % order_code_1
    a = session.post(ht_fh_url).json()
    print(a['message'])

    login_url = 'http://39.108.195.100:8088/groupApi/wechatLogin'
    login_date = {'openId': opemId[0],
                  'version': '1.0'}
    session.post(login_url, login_date).json()
    sh_url = 'http://39.108.195.100:8088/groupApi/order/received'
    sh_data = {'orderCode': order_code_1,
               'version': '1.0'}
    b = session.post(sh_url, sh_data).json()
    print(order_code_1, b['message'])


# 查询等级
def get_user():
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'ldp001',
                   'password': 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(ht_log_url, ht_log_data)

    phone = ['15386174509', '15386174510', '15386174511']
    for i in phone:
        url = 'http://39.108.195.82:8080/groupWebApi/member/list?keys=%s&pageOffset=1&pageSize=10&version=1.0' % i
        user = session.get(url).json()

        jf_url = 'http://39.108.195.82:8080/groupWebApi/score/list/get?keys=%s&version=1.0' % i
        jf = session.get(jf_url).json()
        print(i + ':' + user['data']['datas'][0]['memberTypeStr']+'当前积分：', jf['data']['datas'][0]['totalScore'])


# 修改等级
def set_lv():
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'ldp001',
                   'password': 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(ht_log_url, ht_log_data)

    i = ['15386174508']  # 下单账户
    # i = ['15113597820']  # 一级
    # i = ['18612483433']  # 二级

    url = 'http://39.108.195.82:8080/groupWebApi/member/list?keys=%s&pageOffset=1&pageSize=10&version=1.0' % i[0]
    user = session.get(url).json()
    member_id = user['data']['datas'][0]['memberId']

    set_rank_url = 'http://39.108.195.82:8080/groupWebApi/member/updateMemberGrade?'
    set_rank_data = {'memberId': member_id,
                     'newMemberGrade': '0',
                     'oldMemberGrade': '1',
                     'type': '1',
                     'remark': 'tt',
                     'version': '1.0'}
    rank = session.post(set_rank_url, set_rank_data).json()
    print(rank['message'])
    get_user()


def refund(phone):
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'ldp001',
                   'password': 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(ht_log_url, ht_log_data)

    # 查询订单
    refund_url = 'http://39.108.195.82:8080/groupWebApi/refundOrder/queryReceivedOrderList?' \
                 'orderCode=&keys=&memberPhone=%s&storeId=&namePhone=&expressCode=&skuId=&startDate=&endDate=&greaterTrimestral=0&flag=0&orderStatus=4,9&version=1.0' % phone[0]
    order_code_1 = session.get(refund_url).json()
    totalMoney = order_code_1['data']['datas'][0]['totalMoney']
    freight = order_code_1['data']['datas'][0]['freight']
    memberId = order_code_1['data']['datas'][0]['memberId']
    orderId = order_code_1['data']['datas'][0]['orderId']
    orderCode = order_code_1['data']['datas'][0]['orderCode']
    applyRefundMoneyStr = totalMoney-freight

    url = 'http://39.108.195.82:8080/groupWebApi/refundOrder/saveRefundDapply?'
    data = {'refundReason': '1',
            'refundRemark': '1',
            'dealContent': '1',
            'applyRefundMoneyStr': applyRefundMoneyStr/100,
            'refundType': '1',
            'memberId': memberId,
            'orderId': orderId,
            'orderCode': orderCode,
            'version': '1.0'}
    th = session.post(url, data).json()
    print(th['message'])

    # 确认收货
    url_1 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/allowRefundGoods'
    url_1_data = {'dealContent': '1',
                  'memberId': memberId,
                  'orderId': orderId,
                  'orderCode': orderCode,
                  'version': '1.0'}
    url_1_message = session.post(url_1, url_1_data).json()
    print(url_1_message['message'])

    # 确认物流信息
    url_2 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/uploadMsg'
    url_2_data = {'refundExpressName': 'JD',
                  'refundExpressCode': '11111',
                  'dealContent': '11111',
                  'memberId': memberId,
                  'orderId': orderId,
                  'orderCode': orderCode,
                  'version': '1.0'}
    url_2_message = session.post(url_2, url_2_data).json()
    print(url_2_message['message'])

    # 确认收货
    url_3 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/sureReceiveGoods'
    data_3 = {'dealContent': '1',
              'memberId': memberId,
              'orderId': orderId,
              'orderCode': orderCode,
              'version': '1.0'}
    url_3_message = session.post(url_3, data_3).json()
    print(url_3_message['message'])

    # 确认退款
    url_4 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/updateMoney'
    url_4_data = {'refundMoneyStr': '90',
                  'dealContent': '1',
                  'memberId': memberId,
                  'orderId': orderId,
                  'orderCode': orderCode,
                  'version': '1.0'}
    url_4_message = session.post(url_4, url_4_data).json()
    print(url_4_message['message'])


if __name__ == '__main__':
    opemID = ['ogLGp5UiGQ70tEqpuSqwUhEWB2hM']
    # skuId = ['370535a230114bbb9d41ba6b218ddfaf']  # 开店礼包
    skuId = ['14def0a610db4b8d80b9f3e9ec61915c']
    phone = ['15386174586']
    # # 下单且发货
    purchase(opemID, skuId)
    # time.sleep(10)
    # consignment(opemID, phone)

    # 已收货订单退货退款
    # refund(phone)

    # # 查询等级+
    # get_user()

    # # 修改等级
    # set_lv()

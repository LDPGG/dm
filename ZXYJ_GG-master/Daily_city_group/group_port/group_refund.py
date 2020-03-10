#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14/014 15:13
# @Author  : 刘登攀
# @Site    : 
# @File    : group_refund.py
# @Software: PyCharm
import requests

session = requests.Session()


# 已收货订单退货退款
def refund():
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'yyg',
                   'password': '123456'}
    session.post(ht_log_url, ht_log_data)

    # 查询订单
    refund_url = 'http://39.108.195.82:8080/groupWebApi/refundOrder/queryReceivedOrderList?' \
                 'orderCode=&keys=&memberPhone=15386174586&storeId=&namePhone=&expressCode=&skuId=&startDate=&endDate=&greaterTrimestral=0&flag=0&orderStatus=4&version=1.0'
    order_code_1 = session.get(refund_url).json()
    total_money = order_code_1['data']['datas'][0]['totalMoney']
    freight = order_code_1['data']['datas'][0]['freight']
    member_id = order_code_1['data']['datas'][0]['memberId']
    order_id = order_code_1['data']['datas'][0]['orderId']
    order_code = order_code_1['data']['datas'][0]['orderCode']
    apply_refund_money_str = total_money-freight

    url = 'http://39.108.195.82:8080/groupWebApi/refundOrder/saveRefundDapply?'
    data = {'refundReason': '1',
            'refundRemark': '1',
            'dealContent': '1',
            'applyRefundMoneyStr': apply_refund_money_str,
            'refundType': '1',
            'memberId': member_id,
            'orderId': order_id,
            'orderCode': order_code,
            'version': '1.0'}
    th = session.post(url, data).json()
    print(th['message'])

    # 确认收货
    url_1 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/allowRefundGoods'
    url_1_data = {'dealContent': '1',
                  'memberId': member_id,
                  'orderId': order_id,
                  'orderCode': order_code,
                  'version': '1.0'}
    url_1_message = session.post(url_1, url_1_data).json()
    print(url_1_message['message'])

    # 确认物流信息
    url_2 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/uploadMsg'
    url_2_data = {'refundExpressName': 'JD',
                  'refundExpressCode': '11111',
                  'dealContent': '11111',
                  'memberId': member_id,
                  'orderId': order_id,
                  'orderCode': order_code,
                  'version': '1.0'}
    url_2_message = session.post(url_2, url_2_data).json()
    print(url_2_message['message'])

    # 确认收货
    url_3 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/sureReceiveGoods'
    data_3 = {'dealContent': '1',
              'memberId': member_id,
              'orderId': order_id,
              'orderCode': order_code,
              'version': '1.0'}
    url_3_message = session.post(url_3, data_3).json()
    print(url_3_message['message'])

    # 确认退款
    url_4 = 'http://39.108.195.82:8080/groupWebApi/refundOrder/updateMoney'
    url_4_data = {'refundMoneyStr': '90',
                  'dealContent': '1',
                  'memberId': member_id,
                  'orderId': order_id,
                  'orderCode': order_code,
                  'version': '1.0'}
    url_4_message = session.post(url_4, url_4_data).json()
    print(url_4_message['message'])


if __name__ == '__main__':
    refund()

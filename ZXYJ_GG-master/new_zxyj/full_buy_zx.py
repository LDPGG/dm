#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24/024 10:44
# @Author  : 刘登攀
# @Site    : 
# @File    : full_buy_zx.py
# @Software: PyCharm
import requests
'''
已收货订单退货退款
'''


def buy(order_code):
    session = requests.Session()
    # 登录
    login_url = 'http://39.108.195.48:8080/flyweb/user/login'
    login_data = {'username': 'admin', 'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(login_url, data=login_data)

    # 查询已收货订单
    refundorder_url = 'http://39.108.195.48:8080/flyweb/refundorder/queryOrderList?pager.offset=0&pager.size=10'
    refundorder_data = {'orderCode': order_code,
                        'orderStatus': '4',
                        'payType': '99'
                        }
    refundorder = session.post(refundorder_url, refundorder_data).json()
    order_id = refundorder['data']['datas'][0]['orderId']
    member_id = refundorder['data']['datas'][0]['memberId']
    apply_refund_money_str = refundorder['data']['datas'][0]['totalMoney']-refundorder['data']['datas'][0]['freight']

    # 代替已收货用户申请退货
    refund_order_url = 'http://39.108.195.48:8080/flyweb/refundorder/saveRefundDapply'
    refund_order_data = {'orderId': order_id,
                         'memberId': member_id,
                         'refundReason': '拍错了/信息填写错误',
                         'applyRefundMoneyStr': apply_refund_money_str/100,
                         'refundType': '1',
                         'orderCode': order_code,
                         'refundStatus': '7'
                         }
    refundorder = session.post(refund_order_url, refund_order_data).json()
    print(refundorder['message'])

    # 同意退货
    allow_refund_goods_url = 'http://39.108.195.48:8080/flyweb/refundorder/allowRefundGoods'
    allow_refund_goods_data = {'orderCode': order_code,
                               'orderId': order_id,
                               'memberId': member_id
                               }
    allow_refund_goods = session.post(allow_refund_goods_url, allow_refund_goods_data).json()
    print(allow_refund_goods['message'])

    # 确认物流信息
    up_load_msg_url = 'http://39.108.195.48:8080/flyweb/refundorder/uploadMsg'
    up_load_msg_data = {'orderCode': order_code,
                        'orderId': order_id,
                        'memberId': member_id,
                        'refundGoodsExpressName': '阿达',
                        'refundGoodsExpressCode': '123213213123'
                        }
    up_load_msg = session.post(up_load_msg_url, up_load_msg_data).json()
    print(up_load_msg['message'])

    # 确认收货
    sure_receive_goods_url = 'http://39.108.195.48:8080/flyweb/refundorder/sureReceiveGoods'
    sure_receive_goods_data = {'orderCode': order_code,
                               'orderId': order_id,
                               'memberId': member_id
                               }
    sure_receive_goods = session.post(sure_receive_goods_url, sure_receive_goods_data).json()
    print(sure_receive_goods['message'])

    # 确认退款
    update_money_url = 'http://39.108.195.48:8080/flyweb/refundorder/updateMoney'
    update_money_data = {'orderCode': order_code,
                         'orderId': order_id,
                         'memberId': member_id,
                         'refundMoneyStr': apply_refund_money_str/100,
                         'sellerRemark': 'null',
                         'orderType': '0'}
    update_money = session.post(update_money_url, update_money_data).json()
    print(update_money['message'])


if __name__ == '__main__':
    order_code = '2171578532921157'
    buy(order_code)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14/014 15:09
# @Author  : 刘登攀
# @Site    : 
# @File    : group_purchase.py
# @Software: PyCharm
import requests
from Daily_city_group.group_port.get_token import get_token
import json
import threading


session = requests.Session()


def get_money():
    # ogLGp5Z8THB-t1rPk53QRc-i1Qn0
    login_url = 'http://39.108.195.100:8088/groupApi/wechatLogin'
    login_date = {'openId': 'ogLGp5Z8THB-t1rPk53QRc-i1Qn',
                  'version': '1.0'}
    log = session.post(login_url, login_date).json()
    # print(log)

    url = 'http://39.108.195.100:8088/groupApi/profit/get?version=1.0'
    ppp = session.get(url).json()
    profit_sum_money = ppp['data']['profitSumMoney']
    freeze_sum_money = ppp['data']['freezeSumMoney']
    print('已解冻收益：', profit_sum_money/100, '未解冻收益：', freeze_sum_money/100)


# 购买下单
def purchase_1(conten):
    i = 1
    while i <= conten:
        # 登陆  自己修改为自己账户的openId
        login_url = 'http://39.108.195.100:8088/groupApi/wechatLogin'
        login_date = {'openId': 'sadsadsadsadsa',
                      'version': '1.0'}
        log = session.post(login_url, login_date).json()
        # print(log['message'])

        tj_url = 'http://39.108.195.100:8088/groupApi/order/batchAddOrder?terminal=3&version=1.0&token=%s' % get_token()
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
                                 "skus": [{"skuId": "e436b580f7054b19ab16be8b89b992c1",
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
        print('刘登攀：', tj['message'], i)
        i += 1


threading.Thread(target=purchase_1(5))
# threading.Thread(target=purchase_2(100))
# if __name__ == '__main__':
#     get_money()
#
while 1:
    pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15/015 9:19
# @Author  : 刘登攀
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import threading
import time
import json
import requests
from Daily_city_group.group_port.get_token import get_token

exitFlag = 0

class myBuy(threading.Thread):
    def __init__(self, thread_id, open_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.open_id = open_id
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程：' + self.name)
        purchase_2(self.name, self.open_id, 5)
        print('退出线程：' + self.name)


def purchase_2(name, open_id, counter):
    session = requests.Session()
    i = 1
    while counter:
        if exitFlag:
            name.exit()
        time.sleep(1)
        # 登陆  自己修改为自己账户的openId
        login_url = 'http://39.108.195.100:8088/groupApi/wechatLogin'
        login_date = {'openId': open_id,
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
                                 "skus": [{"skuId": "5a52ce22a7fa47edbd8b3c5c147a8a10",
                                           "quantity": "1"}]
                                 }]
                   }
        tj = session.put(tj_url, data=json.dumps(tj_data), headers=headers).json()
        # print(tj['message'])
        order_code = tj['data'][0]['orderCode']
        # print('订单：'+tj['data'][0]['orderCode']+tj['message'])

        zf_url = 'http://39.108.195.100:8088/groupApi/order/payPwd'
        zf_data = {'orderCode': order_code,
                   'password': 'e10adc3949ba59abbe56e057f20f883e',
                   'version': '1.0',
                   'terminal': '4',
                   'payType': '0'}
        tj = session.post(zf_url, zf_data).json()
        if open_id == 'ogLGp5Z8THB-t1rPk53QRc-i1Qn0':
            print('%s：' % name, tj['message'], i)
        elif open_id == 'ogLGp5UiGQ70tEqpuSqwUhEWB2hM':
            print('%s：' % name, tj['message'], i)
        i += 1
        counter -= 1


# 创建新线程
thread1 = myBuy(1, 'ogLGp5UiGQ70tEqpuSqwUhEWB2hM', '刘登攀', 1)
thread2 = myBuy(2, 'ogLGp5Z8THB-t1rPk53QRc-i1Qn', '马哥', 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3/003 9:48
# @Author  : 刘登攀
# @Site    : 
# @File    : statistics_zxyj.py
# @Software: PyCharm
import requests
'''
统计个人+一级业绩
'''


def performance(phone):
    session = requests.session()
    # 登录
    url_login_test = "http://g.zxyj.com/flyweb/user/login"
    test_login_data = {'username': '刘登攀', "passwd": 'c8837b23ff8aaa8a2dde915473ce0991'}
    session.post(url_login_test, data=test_login_data)

    # 查询个人业绩
    person_url = 'http://g.zxyj.com/flyweb/member/meLevelMoneyList?pager.offset=0&pager.size=200'
    person_data = {'memberPhone': phone, 'orderStatus': '99', 'payType': '99'}
    person = session.post(person_url, person_data).json()
    leve = person['data']['datas']
    member_id = person['data']['datas'][0]['memberId']

    unit = 0
    f_unit = 0
    for i in range(len(leve)):

        order_type = person['data']['datas'][i]['orderType']  # 订单类型
        pay_date = person['data']['datas'][i]['payDate']  # 订单支付时间
        order_from_str = person['data']['datas'][i]['orderFromStr']  # 订单来源
        express_name = person['data']['datas'][i]['expressName']
        order_status_str = person['data']['datas'][i]['orderStatusStr']
        order_code = person['data']['datas'][i]['orderCode']  # 订单状态
        if '2020-01-01 00:00:00' <= pay_date <= '2020-01-31 23:59:59':  # 判断订单支付时间
            if order_type == 11:
                continue
            else:
                if order_from_str == '暂无' or order_status_str == '退款完成' or order_status_str == '已关闭' or order_status_str == '退货完成' or order_status_str == '待付款':
                    continue
                elif order_status_str == '已收货' and express_name != '拆单发货':
                    pay_money = person['data']['datas'][i]['payMoney']  # 支付金额
                    freight = person['data']['datas'][i]['freight']  # 运费
                    discount_coupon = person['data']['datas'][i]['discountCoupon']  # 优惠券金额
                    per_formance = (pay_money - freight + discount_coupon) / 100  # 业绩
                    # print(order_code, per_formance)
                    f_unit += per_formance
                    unit += per_formance
                else:
                    if express_name != '拆单发货':
                        pay_money = person['data']['datas'][i]['payMoney']  # 支付金额
                        freight = person['data']['datas'][i]['freight']  # 运费
                        discount_coupon = person['data']['datas'][i]['discountCoupon']  # 优惠券金额
                        per_formance = (pay_money - freight + discount_coupon) / 100  # 业绩
                        # print(order_code, per_formance)
                        unit += per_formance
                    # print(per_formance)
        else:
            continue
    print('手机号：%s 个人业绩:' % phone, round(unit, 2))
    print('已收货个人业绩：', round(f_unit, 2))

    # 查询大众家人业绩
    folk_url = 'http://g.zxyj.com/flyweb/member/firstLevelMoneyList?pager.offset=0&pager.size=200'
    folk_data = {'memberId': member_id, 'type': '99'}
    folk = session.post(folk_url, folk_data).json()
    merit = folk['data']['datas']
    mass = 0
    y_mass = 0
    for l in range(len(merit)):
        retail_money = folk['data']['datas'][l]['retailMoney']  # 零售金额
        join_money = folk['data']['datas'][l]['joinMoney']  # 加盟金额
        if retail_money > 0 > join_money:
            join_money = abs(join_money)  # 避免旧数据导致统计错误 使用优惠券后加盟金额显示负数问题
        create_date = folk['data']['datas'][l]['createDate']  # 操作时间
        order_code = folk['data']['datas'][l]['orderCode']  # 订单号
        if '2020-01-01 00:00:00' <= create_date <= '2020-01-31 23:59:59':  # 判断业绩的创建时间
            # 查询出所有订单的状态
            url = 'http://g.zxyj.com/flyweb/order/queryOrderList?pager.offset=0&pager.size=10'
            data = {'orderProfitStatus': '99', 'orderprofit': '1', 'orderCode': order_code, 'falg': '0', 'orderStatus': '99', 'payType': '99',
                    'isStore': '0'}
            code = session.post(url, data).json()
            pay_date = code['data']['datas'][0]['payDate']  # 订单支付时间
            expressName = code['data']['datas'][0]['expressName']

            if pay_date >= '2020-01-01 00:00:00':  # 避免上月订单本月退款
                total = (retail_money+join_money)/100
                mass += total
                # print(order_code, total)
                # print(total)
                # print(order_code, code['data']['datas'][0]['orderStatusStr'], total)
                if code['data']['datas'][0]['orderStatusStr'] == '已收货' and expressName != '拆单发货':
                    y_mass += total
                    # print(total)
                    # print(order_code, total)
            else:
                continue
            # print(order_code, total)
        else:
            continue
    print('手机号：%s 大众家人业绩:' % phone, round(mass, 2))
    print('已收货家人业绩：', round(y_mass, 2))
    print('个人+y一级总业绩：%s' % round(unit+mass, 2))


if __name__ == '__main__':
    phone = '18741898058'
    performance(phone)
'''
64278577
'''
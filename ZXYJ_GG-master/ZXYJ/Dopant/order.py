# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 下午 2:02
# @Author  : 刘登攀阿！！
# @FileName: ht.py
# @Software: PyCharm
import requests
import re
import time
'''
购买-发货-收货
'''


class Order(object):
    def __init__(self):
        self.path = r'C:\\Users\Administrator\Desktop\ppp.txt'
        # 读取记事本内容
        self.phones = open(self.path, 'r').readlines()
        # 存储cookies
        self.session = requests.Session()

    # 购买
    def buy(self):
        session = requests.Session()
        sku = '4ad6d9e2ddb24bea8e631e12947b47f9'
        for phones in self.phones:
            phone = phones.strip()
            print(phone)
            # 登陆
            try:
                url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"
                test_login_data = {'username': phone, "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
                login = session.post(url_login_test, data=test_login_data).json()
                print(login['data']['phone'])
                member_id = login['data']['memberId']

            except:
                url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"
                test_login_data = {'username': phone, "password": 'dc483e80a7a0bd9ef71d8cf973673924', "origin": '1'}
                login = session.post(url_login_test, data=test_login_data).json()
                print(login['data']['phone'])
                member_id = login['data']['memberId']

            # 获取收货地址

            url_get_address = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
            get_address = session.get(url_get_address, data='').json()
            if get_address['data']['datas']:
                # 生成订单
                url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"

                # 店主礼包
                # add_data = '{"orderFrom":1,"couponId":"","orderType":4,"remark":"","products":[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' % (skuId, quantity, addressId)
                # 普通产品
                address_id = get_address['data']['datas'][0]['addressId']
                add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":"1"}],"addressId":"%s"}' % (sku, address_id)
                pay_order = session.post(url_add, data=add_data).json()
                print(pay_order['message'])
                # 获取待支付订单列表
                url_get_order = "http://39.108.195.82:8080/flyapi/popupOrder/getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
                session.get(url_get_order, data='').json()
                # # 设置支付密码
                # url_set_pwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
                # set_pwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
                # session.post(url_set_pwd, data=set_pwd_data)
                #
                # # 验证支付密码
                # url_give_pwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
                # session.get(url_give_pwd, data='').json()
                #
                # # 支付订单
                # url_pay_pwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
                # pay_pwd_data = {'orderCode': pay_order['data']['orderCode'], "password": 'e10adc3949ba59abbe56e057f20f883e'}
                # pay_pwd = session.post(url_pay_pwd, data=pay_pwd_data).json()
                # print(pay_pwd['message'])
            else:
                # 添加新收货地址
                url_address_test = "http://39.108.195.82:8080/flyapi/address/add?version=1.0"
                test_address_data = {'phone': phone,
                                     'provinceId': "130000", 'cityId': '130300',
                                     'districtId': '130303', 'districtName': '白云区',
                                     'cityName': '广州市', 'provinceName': '广东省',
                                     'detail': '不想写', 'isDefault': '1',
                                     'contact': 'weiwen', 'memberId': member_id}
                session.post(url_address_test, data=test_address_data)
                Order().buy()

    # 后台发货
    def shipments(self):
        for phone in self.phones:
            # for phone in phones:
            # # 清除掉记事本里面的\n
            p = phone.replace('\n', '')
            # 登录
            post_url = 'http://39.108.195.48:8080/flyweb/user/login'
            post_login = {'username': 'admin', 'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
            self.session.post(post_url, data=post_login)
            # 获取待发货订单列表
            post_list_url = 'http://39.108.195.48:8080/flyweb/order/queryOrderList?pager.offset=0&pager.size=10'
            post_list_login = {'orderProfitStatus': '99',
                               'orderprofit': '1',
                               'falg': '0',
                               'memberPhone': p,
                               'orderStatus': '2',
                               'payType': '99',
                               'isStore': '0'}
            post_lis_url_login = self.session.post(post_list_url, data=post_list_login).json()
            order_code = re.findall("'orderCode': '(.*?)'", "%s" % post_lis_url_login)
            # 进入订单详情
            try:
                post_affirm_url = r'http://39.108.195.48:8080/flyweb/order/ship'
                post_affirm_login = {'orderCode': order_code[0],
                                     'expressNo': 'ZTO',
                                     'expressName': '中通',
                                     'expressCode': '75118724696295',
                                     'sellerRemark': ''}
                affirm = self.session.post(post_affirm_url, data=post_affirm_login)
                get_affirm = affirm.json()
                state = re.findall("'message': '(.*?)'", "%s" % get_affirm)
                print('%s的订单%s%s' % (p, order_code[0], state))
            except:
                print('%s没有待发货的订单' % p)
                continue

    # 发货
    def delivery(self):
        for phone in self.phones:
            # for phone in phones:
            # # 清除掉记事本里面的\n
            p = phone.replace('\n', '')
            # 用户登录
            url_login = 'http://39.108.195.82:8080/flyapi/login?version=1.0'
            post_login = {'username': p,
                          "password": 'e10adc3949ba59abbe56e057f20f883e',
                          "origin": '1'}
            self.session.post(url_login, data=post_login)
            # 獲取已發貨的訂單列表jk
            url_deliver = 'http://39.108.195.82:8080/flyapi/order/list/search?keyword=&status=3&' \
                          'pageOffset=1&pageSize=15&version=1.0&terminal=1'
            get_take = self.session.get(url_deliver).json()
            print(get_take)
            order_code = re.findall("orderCode\': \'(.*?)'", "%s" % get_take)
            # # 確認收貨
            url_take = 'http://39.108.195.82:8080/flyapi/order/received?version=1.0&terminal=1'
            try:
                post_take = {'orderCode': order_code[0]}
                oo = self.session.post(url_take, data=post_take)
                oo_url = oo.json()
                post_login_oo = re.findall("'message': '(.*?)'", "%s" % oo_url)
                print('%s的订单%s%s' % (p, order_code[0], post_login_oo))
            except:
                print(p + '未找到已發貨訂單')
                continue


if __name__ == '__main__':
    Order().buy()
    time.sleep(2)
    Order().shipments()
    # time.sleep(2)
    # Order().delivery()


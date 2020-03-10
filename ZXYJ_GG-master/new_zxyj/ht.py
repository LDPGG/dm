# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 下午 2:02
# @Author  : 刘登攀阿！！
# @FileName: ht.py
# @Software: PyCharm
import requests
import re
'''
发货-收货
'''


def ht(phone):

    session = requests.Session()

    '''
    跳转后台发货
    '''
    # 登录
    post_url = 'http://39.108.195.48:8080/flyweb/user/login'
    post_login = {'username': 'admin', 'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
    session.post(post_url, data=post_login)
    # 获取待发货订单列表
    post_list_url = 'http://39.108.195.48:8080/flyweb/order/queryOrderList?pager.offset=0&pager.size=10'
    post_list_login = {'orderProfitStatus': '99',
                       'orderprofit': '1',
                       'falg':'0',
                       'memberPhone': phone,
                       'orderStatus': '2',
                       'payType': '99',
                       'isStore': '0'}
    post_lis_url_login = session.post(post_list_url, data=post_list_login)
    get_orderCode = post_lis_url_login.json()
    orderCode = re.findall("'orderCode': '(.*?)'", "%s" %get_orderCode)
    # # 进入订单详情
    try:
        post_affirm_url = 'http://39.108.195.48:8080/flyweb/order/ship'
        post_affirm_login = {'orderCode': orderCode[0],
                             'expressNo': 'ZTO',
                             'expressName': '中通',
                             'expressCode': '12345',
                             'sellerRemark': ''}
        affirm = session.post(post_affirm_url, data=post_affirm_login)
        get_affirm = affirm.json()
        state = re.findall("'message': '(.*?)'", "%s" % get_affirm)
        print('%s的订单%s%s' % (phone, orderCode[0],state))

    except:
        print('%s没有待发货的订单' % p)
    '''
    跳转前端确认收货
    '''
    # 用户登录
    url_login = 'http://39.108.195.82:8080/flyapi/login?version=1.0'
    post_login = {'username': phone,
                  "password": 'e10adc3949ba59abbe56e057f20f883e',
                  "origin": '1'}
    session.post(url_login, data=post_login)
    # 獲取已發貨的訂單列表
    url_deliver = 'http://39.108.195.82:8080/flyapi/order/list/search?keyword=&status=3&' \
                  'pageOffset=1&pageSize=15&version=1.0&terminal=1'
    gettake = session.get(url_deliver)
    g_gettake = gettake.json()
    orderCode = re.findall("orderCode\': \'(.*?)'", "%s" % g_gettake)
    # 確認收貨
    url_take = 'http://39.108.195.82:8080/flyapi/order/received?version=1.0&terminal=1'
    try:
        post_take = {'orderCode': orderCode[0]}
        oo = session.post(url_take, data=post_take)
        oo_url = oo.json()
        post_login_oo = re.findall("'message': '(.*?)'", "%s" % oo_url)
        print('%s的订单%s%s' % (phone, orderCode[0], post_login_oo))
        print('--------------------------------------------------')
    except:
        print(phone + '未找到已發貨訂單')


if __name__ == '__main__':
    phone = '15386174533'
    ht(phone)

#登陆-购买商品
import http

import requests
import re
'''
购买商品
'''

#登陆
f = r'C:\Users\Administrator\Desktop\buy_phone.txt' #你所要打开的特定目录的特定文件
phone = open(f, 'r').readlines()               #把文件中的每一行作为一个元素添加到列表phone上
#skuId = 'f12876bbad314d649d970da9379c0e7a'     #购买商品的skuId ##店主礼包
skuId = '026e4efd0dc6495ab3ebcd63b95ce8d9'   #普通商品
session = requests.Session()                   #存储cookies

# 迭代txt文件的phone
for phone in phone:
    session = requests.Session()  # 存储cookies
    url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"  #用户登陆
    test_login_data = {'username': phone, "password": 'dc483e80a7a0bd9ef71d8cf973673924', "origin": '1'}
    login = session.post(url_login_test, data=test_login_data) #用post请求获得session
    memberId = re.findall(r"memberId\":\"(.*?)\"", "%s" % login.text)  # getMemberId
    # print(len(memberId)) 因为txt有空格导致//IndexError: list index out of range//
    # print(memberId[0])
    # 添加新收货地址
    url_address_test = "http://39.108.195.82:8080/flyapi/address/add?version=1.0"
    test_address_data = {'phone': phone,
                         'provinceId': "130000", 'cityId': '130300',
                         'districtId': '130303', 'districtName': '白云区',
                         'cityName': '广州市', 'provinceName': '广东省',
                        'detail': '不想写', 'isDefault': '1',
                        'contact': 'weiwen', 'memberId': memberId[0]}
    response_address = session.post(url_address_test, data=test_address_data)
    # print(response_address.text)

    #获取收货地址(写一个判断没有再添加收货地址)△怎么获得未加密的cookies，以字典代入
    url_getAddress = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
    getAddress = session.get(url_getAddress, data='')
    userAddress = getAddress.json()
    # print(userAddress)
    address = re.findall(r"addressId': '(.*?)'", "%s" % userAddress)
    addressId = address[0]
    # print(addressId)

    #POST http://39.108.195.82:8080/flyapi/expressPrice/calc?version=1.0
    # url_calc = "http://39.108.195.82:8080/flyapi/expressPrice/calc?version=1.0"
    quantity = '1'
    # calc_data = '{"products":[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' \
    #         % (skuId, quantity, addressId)
    # calc = session.post(url_calc, data=calc_data)
    # memberId = re.findall(r"memberId\"\:\"(.*?)\"", "%s" % login.text)  # getMemberId

    # 生成订单
    url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"
    add_data = '{"orderFrom":1,"couponId":"","orderType":4,"remark":"","products":' \
               '[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' % (skuId, quantity, addressId) #店主礼包
    # add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":%s}],
    # "addressId":"%s"}' % (skuId, quantity, addressId) #普通产品
    add = session.post(url_add, data=add_data)
    payPwd_orderCode = re.findall(r"orderCode\":\"(.*?)\"", "%s" % add.text)

    # 获取待支付订单列表
    url_getPopupOrderList = "http://39.108.195.82:8080/flyapi/popupOrder/" \
                            "getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
    getPopupOrderList = session.get(url_getPopupOrderList, data='')
    m_getPopupOrderList = getPopupOrderList.json()
    orderCode = re.findall(r"orderCode\': \'(.*?)'", "%s" % m_getPopupOrderList)

    # 设置支付密码
    url_setPayPwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
    setPayPwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
    setPayPwd = session.post(url_setPayPwd, data=setPayPwd_data)

    # 验证支付密码
    url_givePayPwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
    givePayPwd = session.get(url_givePayPwd, data='')
    m_givePayPwd = givePayPwd.json()

    url_payPwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
    payPwd_data = {'orderCode': '%s' % payPwd_orderCode[0], "password": 'e10adc3949ba59abbe56e057f20f883e'}
    payPwd = session.post(url_payPwd, data=payPwd_data)
    print('%s付款成功' % phone)
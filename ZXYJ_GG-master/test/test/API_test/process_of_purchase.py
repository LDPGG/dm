#登陆-购买商品
#把post请求全部撸一遍，没有数据就去get请求找
import http

import requests
import json
import xlwt
import re
import cookiejar
import urllib.request, urllib.parse, urllib.error

#登陆
f = r'C:\\Users\\duan\\Desktop\\buy_phone.txt' #你所要打开的特定目录的特定文件
phone = open(f, 'r').readlines()               #把文件中的每一行作为一个元素添加到列表l1上
session = requests.Session()                   #存储cookies

url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"  #用户登陆
test_login_data={'username': phone, "password": 'dc483e80a7a0bd9ef71d8cf973673924', "origin": '1'}
login = session.post(url_login_test, data=test_login_data) #用post请求获得cookies
memberId = re.findall(r"memberId\"\:\"(.*?)\"", "%s" % login.text)  # getMemberId
# memberId = re.findall(r"\"message\"\:\"(.*?)！\"", "%s" % response.text)
# print(memberId[0])

# print(response.text)
# read = json.loads(response.text) #把JSON反序列化为Python对象

# #添加到足迹
# url_addViewRecord_test = "http://39.108.195.82:8080/flyapi/viewHistory/addViewRecord?version=1.0"  #??
# test_addViewRecord_data = {'memberId': memberId[0], "skuId": '246911a2472940319ad74228f2ba1ce0'}
# # 给skuId(怎么通过skuid查产品？？GET http://39.108.195.82:8080/flyapi/product/skuDetail?skuId=22c16a15d6d54361a7c1d3e0c3f2a88c&version=1.0)
# # header_addViewRecord = {
# #     'User-Agent': 'okhttp/3.8.0',
# #     'Accept-Encoding': 'gzip, deflate',
# #     'Content-Type': 'application/x-www-form-urlencoded',
# #     'cookie': "%s" % (getCookie[0])}
# response_addViewRecord = session.post(url_addViewRecord_test, data=test_addViewRecord_data)
# print(response_addViewRecord.text)

# 添加新收货地址
# phone=&provinceId=130000&cityId=130300&
# districtId=130303&districtName=&
# cityName=&provinceName=&detail=&isDefault=0&contact=&memberId=
url_address_test = "http://39.108.195.82:8080/flyapi/address/add?version=1.0"  #??
test_address_data = {'phone': phone,
                     'provinceId': "130000", 'cityId': '130300',
                     'districtId': '130303', 'districtName': '白云区',
                     'cityName': '广州市', 'provinceName': '广东省',
                     'detail': '不想写', 'isDefault': '1',
                     'contact': 'weiwen', 'memberId': memberId[0]}
# 给skuId(怎么通过skuid查产品？？GET http://39.108.195.82:8080/flyapi/product/skuDetail?skuId=22c16a15d6d54361a7c1d3e0c3f2a88c&version=1.0)
# header_address = {
#     'User-Agent': 'okhttp/3.8.0',
#     'Accept-Encoding': 'gzip, deflate',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'cookie': "%s" % (getCookie[0])}
response_address = session.post(url_address_test, data=test_address_data)
# print(response_address.text)

#获取收货地址(写一个判断没有再添加收货地址)△怎么获得未加密的cookies，以字典代入
#http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0
url_getAddress = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
getAddress = session.get(url_getAddress, data='')
userAddress = getAddress.json()
# print(userAddress)
address = re.findall(r"addressId': '(.*?)'", "%s" % userAddress) #(.*?)可以匹配多个addressId组成列表
addressId = address[0]
# print(addressId)

#POST http://39.108.195.82:8080/flyapi/expressPrice/calc?version=1.0
url_calc = "http://39.108.195.82:8080/flyapi/expressPrice/calc?version=1.0"
skuId = '3e554fd744724ed48e2be974ac0e11f7'
quantity = '1'
calc_data = '{"products":[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' \
            % (skuId, quantity, addressId)
# print(calc_data)
calc = session.post(url_calc, data=calc_data)
# print(calc.text)
memberId = re.findall(r"memberId\"\:\"(.*?)\"", "%s" % login.text)  # getMemberId

#POST http://39.108.195.82:8080/flyapi/order/add?version=1.0 生成订单
url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"
add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' % (skuId, quantity, addressId)
add = session.post(url_add, data= add_data)
# print(add.text)
#获取payPwd_orderCode
payPwd_orderCode = re.findall(r"orderCode\":\"(.*?)\"", "%s" % add.text)
# print(payPwd_orderCode)


#GET http://39.108.195.82:8080/flyapi/order/getOrderStatusCount?version=1.0 #等待支付订单
url_getOrderStatusCount = "http://39.108.195.82:8080/flyapi/order/getOrderStatusCount?version=1.0"
getOrderStatusCount = session.get(url_getOrderStatusCount, data='')
m_getOrderStatusCount = getOrderStatusCount.json()
# print(m_getOrderStatusCount)
# address = re.findall(r"addressId': '(.*?)'", "%s" % userAddress) #(.*?)可以匹配多个addressId组成列表
# addressId = address[0]
# print(addressId)

# GET http://39.108.195.82:8080/flyapi/paypwd/exit?version=1.0 #支付密码


# GET http://39.108.195.82:8080/flyapi/popupOrder/getPopupOrderList?pageOffset=1&pageSize=10&version=1.0 #获取待支付订单列表
url_getPopupOrderList = "http://39.108.195.82:8080/flyapi/popupOrder/getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
getPopupOrderList = session.get(url_getPopupOrderList, data='')
m_getPopupOrderList = getPopupOrderList.json()
orderCode = re.findall(r"orderCode\': \'(.*?)'", "%s" % m_getPopupOrderList)
print(m_getPopupOrderList)
print(orderCode)

# 设置支付密码
# POST http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1
# pay_password=e10adc3949ba59abbe56e057f20f883e   //------123456-------
url_setPayPwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
setPayPwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
setPayPwd = session.post(url_setPayPwd, data=setPayPwd_data)
print(setPayPwd.text)

# 验证支付密码
# GET http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1
url_givePayPwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
givePayPwd = session.get(url_givePayPwd, data='')
m_givePayPwd = givePayPwd.json()
# print(givePayPwd.text)

# POST http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0 #支付订单
# orderCode=%24%7BorderCode%7D&password=e10adc3949ba59abbe56e057f20f883e
# nbPayPwd = int(payPwd_orderCode[0])
url_payPwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
payPwd_data = {'orderCode': '%s' % payPwd_orderCode[0], "password": 'e10adc3949ba59abbe56e057f20f883e'}
payPwd = session.post(url_payPwd, data=payPwd_data)
# print(payPwd.text)
# print(payPwd_orderCode[0])
# orderCode":"(.*)"}}
#----------------------抓包看哪里问题(不细心导致的，本来就是错，还一直试)
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
cookies = session.post(url_login_test, data=test_login_data) #获得cookies
print(cookies.text)

#获取收货地址(写一个判断没有再添加收货地址)△怎么获得未加密的cookies，以字典代入
#http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0
url_getAddress = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
getAddress = session.get(url_getAddress, data='')
userAddress = getAddress.json()
print(userAddress)

#添加新收货地址
#phone=&provinceId=130000&cityId=130300&
# districtId=130303&districtName=&
# cityName=&provinceName=&detail=&isDefault=0&contact=&memberId=
# url_address_test = "http://39.108.195.82:8080/flyapi/address/add?version=1.0"  #??
# test_address_data = {'phone': phone,
#                      'provinceId': "130000", 'cityId': '130300',
#                      'districtId': '130303', 'districtName': '白云区',
#                      'cityName': '广州市', 'provinceName': '广东省',
#                      'detail': '不想写', 'isDefault': '1',
#                      'contact': 'weiwen', 'memberId': memberId[0]}
# # 给skuId(怎么通过skuid查产品？？GET http://39.108.195.82:8080/flyapi/product/skuDetail?skuId=22c16a15d6d54361a7c1d3e0c3f2a88c&version=1.0)
# header_address = {
#     'User-Agent': 'okhttp/3.8.0',
#     'Accept-Encoding': 'gzip, deflate',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'cookie': "%s" % (getCookie[0])}
# response_address = requests.post(url_address_test, data=test_address_data, headers=header_address)
# print(response_address.text)


#查询家人订单

import requests
import json
import xlwt
import re
import cookiejar
import urllib.request, urllib.parse, urllib.error

session = requests.Session()                   #存储cookies
url_login_test = "http://gs.zxyjsc.com/flyweb/user/login"  #用户登陆
test_login_data = {'username': '测试', "passwd": '43cbed803b9824e1b94613d78cf6a6d3'}
login = session.post(url_login_test, data=test_login_data) #用post请求获得cookies
# print(login.text)


url_youhuquan_test = "http://gs.zxyjsc.com/flyweb/product/queryCouponList?pager.offset=0&pager.size=10"
test_youhuiquan_data = {'title': '', "productName": '', "couponType": '99', "storeId": '836ba6ac662147a199333319db4b45b9', "type": '99'}
youhuiquan = session.post(test_youhuiquan_data, data=test_youhuiquan_data)
print(youhuiquan)

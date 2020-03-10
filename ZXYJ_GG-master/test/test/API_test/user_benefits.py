#查询家人订单

import requests
import json
import xlwt
import re
import cookiejar
import urllib.request, urllib.parse, urllib.error

#登陆
f = r'C:\\Users\\duan\\Desktop\\user_benefits.txt' #你所要打开的特定目录的特定文件
phone = open(f, 'r').readlines()               #把文件中的每一行作为一个元素添加到列表l1上
session = requests.Session()                   #存储cookies

url_login_test = "http://gs.zxyjsc.com/flyweb/user/login"  #用户登陆
test_login_data = {'username': '测试', "passwd": '43cbed803b9824e1b94613d78cf6a6d3'}
login = session.post(url_login_test, data=test_login_data) #用post请求获得cookies
# print(login.text)

#获得查询条数
url_queryProfitList = 'http://gs.zxyjsc.com/flyweb/member/queryProfitList?pager.offset=0&pager.size=300'
test_queryProfitList_data = {'memberId': '1e3325fd83ed452cb1d63ec392b2bb08', "orderCode": '', 'memberPhone': '', "type": ''}       #aaa.replace(/\[a-z0-9]/g,'')
queryProfitList = session.post(url_queryProfitList, data=test_queryProfitList_data)
# print(queryProfitList.text)
o_memberId = re.findall(r"datas\":(.*?)],\"pageOffset", "%s" % queryProfitList.text)  # getMemberId
t_memberId = re.findall(r"{(.*?)}", "%s" % o_memberId)
# memberId = re.findall(r"\"message\"\:\"(.*?)！\"", "%s" % response.text)
# print(memberId[0])

print(t_memberId)
i = []
for i in t_memberId:
    freezeProfitMoney = re.findall(r"freezeProfitMoney\":(.*?),", "%s" % i) #收益金额
    a1 = int(freezeProfitMoney[0])/100
    orderCode = re.findall(r"orderCode\":\"(.*?)\"", "%s" % i)  # 订单号
    createDate = re.findall(r"createDate\":\"(.*?)\"", "%s" % i)  # 操作时间
    statusStr = re.findall(r"statusStr\":\"(.*?)\"", "%s" % i)  # 状态
    srelevancePhone = re.findall(r"relevancePhone\":\"(.*?)\"", "%s" % i)  # 下单用户手机号
    orderMemberName = re.findall(r"orderMemberName\":\"(.*?)\"", "%s" % i)  # 下单用户姓名
    level = re.findall(r"level\":(.*?),", "%s" % i)  # 第几层收益
    tatusStr = re.findall(r"statusStr\":\"(.*?)\"", "%s" % i)  # 第几层收益
    if a1 < 0:
        user_data = r"第几层收益:%s下单用户手机号:%s下单用户姓名:%s订单号:%s收益金额:%s第几层收益:%s状态:%s操作时间:%s" % \
                    (tatusStr, srelevancePhone, orderMemberName, orderCode, a1, level, statusStr, createDate)
        print(user_data)



# "freezeId":"631416b97d6941bea63e8c1209a8b46c",
# "sortIndex":13659,
# "memberBean":"",
# "type":1,
# "orderId":"01e3c9ccff5540deafec3614774a7526",
# "orderMemberId":"8d40006d7f164eed8150591f55123c91",
# "orderCode":"1451525912829839",
# "orderMoney":9000,
# "freezeProfitMoney":156,
# "freezeSumMoney":76896,
# "profitSumMoney":2779445,
# "profitTime":"2018-05-0717: 31: 01",
# "status":0,
# "level":2,
# "createDate":"2018-05-0717: 31: 01",
# "relevancePhone":"15229901511",
# "orderMemberName":"吴晨",
# "orderMemberNickName":"安安北鼻?",
# "typeStr":"推广奖",
# "statusStr":"未解冻"







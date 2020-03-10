# 批量用户后台充钱

import requests
import json
import xlwt
import re
import cookiejar
import urllib.request, urllib.parse, urllib.error
'''
    添加零钱
'''

#登陆
f = r'C:\\Users\\Administrator\\Desktop\\mphone.txt' #你所要打开的特定目录的特定文件
phoneBad = open(f, 'r').readlines()               #把文件中的每一行作为一个元素添加到列表l1上

for nowPhone in phoneBad:
    session = requests.Session()                   #存储cookies
    phone = nowPhone.strip()
    # POST http://39.108.195.48:8080/flyweb/user/login #用户登陆
    url_login_test = "http://39.108.195.48:8080/flyweb/user/login"
    test_login_data = {'username': 'admin', "passwd": 'e10adc3949ba59abbe56e057f20f883e'}
    login = session.post(url_login_test, data=test_login_data) #用post请求获得session

    # POST http://39.108.195.48:8080/flyweb/member/queryMemberListForUpdate?pager.offset=0&pager.size=10
    url_queryMemberList = 'http://39.108.195.48:8080/flyweb/member/queryMemberListForUpdate?pager.offset=0&pager.size=10'
    test_queryMemberList_data = {'refermemberId': '', "keys": '%s' % phone, 'memberId': ''}
    queryMemberList = session.post(url_queryMemberList, data=test_queryMemberList_data)
    getMemberId = re.findall(r"memberId\":\"(.*?)\"", "%s" % queryMemberList.text)  # getMemberId
    memberId = getMemberId[0]

    # POST http://39.108.195.48:8080/flyweb/member/addMemberMoney
    url_addMemberMoney = 'http://39.108.195.48:8080/flyweb/member/addMemberMoney'
    test_addMemberMoney_data = {'memberId': '%s' % memberId, "money": '10000', 'type': '6', 'changeReason': '', 'phone': '%s' % phone}
    addMemberMoney = session.post(url_addMemberMoney, data=test_addMemberMoney_data)
    # print(addMemberMoney.text)

    # POST http://39.108.195.48:8080/flyweb/member/changeExamineList?pager.offset=0&pager.size=1 #getChangeId
    url_getChangeId = 'http://39.108.195.48:8080/flyweb/member/changeExamineList?pager.offset=0&pager.size=1'
    test_getChangeId_data = {'userPhone': '%s' % phone, "sysPhone": '', 'type': '99'}
    getChangeId = session.post(url_getChangeId, data=test_getChangeId_data)
    ChangeId = re.findall(r"changeId\":\"(.*?)\"", "%s" % getChangeId.text)  # getMemberId
    # print(ChangeId[0])

    # POST http://39.108.195.48:8080/flyweb/member/updateChangeExamine
    url_updateChangeExamine = 'http://39.108.195.48:8080/flyweb/member/updateChangeExamine'
    test_updateChangeExamine_data = {'changeId': '%s' % ChangeId[0], "status": '1'}
    updateChangeExamine = session.post(url_updateChangeExamine, data=test_updateChangeExamine_data)
    print(phone)
    print(updateChangeExamine.text)


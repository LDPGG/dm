# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 0013 上午 10:54
# @Author  : 刘登攀阿！！
# @FileName: TTTTTT.py
# @Software: PyCharm
import requests
import json
import re

def zc():
    # 你所要打开的特定目录的特定文件
    filepath = r'C:\Users\Administrator\Desktop\ppp.txt'
    # 把文件中的每一行作为一个元素添加到列表phone上
    phone = open(filepath, 'r').readlines()
    phone_Inv = input('输入上级手机号：')
    # 怎么迭代的传入多个参数
    for phone_userBad in phone:
        phone_user = phone_userBad.strip()
        # 查邀请人号
        url_invitationCode = 'http://39.108.195.82:8080/flyapi/user/' \
                             'getMemberInfoByInviteCode?inviteCode=%s&version=1.0' % phone_Inv
        url_newloginer = "http://39.108.195.82:8080/flyapi/user/add?version=1.0"
        # 拿inviteCode邀请人号码
        r = requests.get(url_invitationCode, data='', headers='', cookies='')
        read = json.loads(r.text)
        en = (read['data']['inviteCode'])
        print(phone_user)
        print(en)
        # 批量注册用户
        test_data = {'password': 'dc483e80a7a0bd9ef71d8cf973673924', "invitationCode": en,
                     "phone": phone_user, 'checkNumber': "20160920"}
        header = {
            'User-Agent': 'okhttp/3.8.0',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8d',
            'cookie': ""}
        # 上面填入jmeter抓到的cookie
        response = requests.post(url_newloginer, data=test_data, headers=header)
        read = json.loads(response.text)
        print(read)


# 加钱
def jq():
    f = r'C:\Users\Administrator\Desktop\ppp.txt'  # 你所要打开的特定目录的特定文件
    phoneBad = open(f, 'r').readlines()  # 把文件中的每一行作为一个元素添加到列表l1上
    for nowPhone in phoneBad:
        session = requests.Session()  # 存储cookies
        phone = nowPhone.strip()
        # POST http://39.108.195.48:8080/flyweb/user/login #用户登陆
        url_login_test = "http://39.108.195.48:8080/flyweb/user/login"
        test_login_data = {'username': 'admin', "passwd": 'e10adc3949ba59abbe56e057f20f883e'}
        login = session.post(url_login_test, data=test_login_data)  # 用post请求获得session

        # POST http://39.108.195.48:8080/flyweb/member/queryMemberListForUpdate?pager.offset=0&pager.size=10
        url_queryMemberList = 'http://39.108.195.48:8080/flyweb/member/queryMemberListForUpdate?pager.offset=0&pager.size=10'
        test_queryMemberList_data = {'refermemberId': '', "keys": '%s' % phone, 'memberId': ''}
        queryMemberList = session.post(url_queryMemberList, data=test_queryMemberList_data)
        getMemberId = re.findall(r"memberId\":\"(.*?)\"", "%s" % queryMemberList.text)  # getMemberId
        memberId = getMemberId[0]

        # POST http://39.108.195.48:8080/flyweb/member/addMemberMoney
        url_addMemberMoney = 'http://39.108.195.48:8080/flyweb/member/addMemberMoney'
        test_addMemberMoney_data = {'memberId': '%s' % memberId, "money": '999999', 'type': '6', 'changeReason': '',
                                    'phone': '%s' % phone}
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


# 购买产品
def gm():
    # 登陆
    f = r'C:\Users\Administrator\Desktop\ppp.txt'  # 你所要打开的特定目录的特定文件
    phone = open(f, 'r').readlines()  # 把文件中的每一行作为一个元素添加到列表phone上
    skuId = 'f12876bbad314d649d970da9379c0e7a'  # 购买商品的skuId ##店主礼包
    # skuId = '6421f28573c34eaf950ef2a3c06b2815'   #普通商品
    session = requests.Session()  # 存储cookies

    # 迭代txt文件的phone4
    for phonea in phone:
        phone = phonea.strip('\n')
        session = requests.Session()  # 存储cookies
        url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"  # 用户登陆
        test_login_data = {'username': phone, "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
        login = session.post(url_login_test, data=test_login_data)  # 用post请求获得session
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

        # 获取收货地址(写一个判断没有再添加收货地址)△怎么获得未加密的cookies，以字典代入
        url_getAddress = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
        getAddress = session.get(url_getAddress, data='')
        userAddress = getAddress.json()
        # print(userAddress)
        address = re.findall(r"addressId': '(.*?)'", "%s" % userAddress)
        addressId = address[0]
        # print(addressId)

        # POST http://39.108.195.82:8080/flyapi/expressPrice/calc?version=1.0
        # url_calc = "http://39.108.195.82:8080/flyapi/expressPrice/calc?version=1.0"
        quantity = '1'
        # calc_data = '{"products":[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' \
        #         % (skuId, quantity, addressId)
        # calc = session.post(url_calc, data=calc_data)
        # memberId = re.findall(r"memberId\"\:\"(.*?)\"", "%s" % login.text)  # getMemberId

        # 生成订单
        url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"
        add_data = '{"orderFrom":1,"couponId":"","orderType":4,"remark":"","products":' \
                   '[{"skuId":"%s","quantity":%s}],"addressId":"%s"}' % (skuId, quantity, addressId)  # 店主礼包
        # add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":%s}],' \
        #            '"addressId":"%s"}' % (skuId, quantity, addressId) #普通产品
        add = session.post(url_add, data=add_data)
        print(add)
        payPwd_orderCode = re.findall(r"orderCode\":\"(.*?)\"", "%s" % add.text)
        # print(payPwd_orderCode)

        # 获取待支付订单列表
        url_getPopupOrderList = "http://39.108.195.82:8080/flyapi/popupOrder/" \
                                "getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
        getPopupOrderList = session.get(url_getPopupOrderList, data='')
        m_getPopupOrderList = getPopupOrderList.json()
        orderCode = re.findall(r"orderCode\': \'(.*?)'", "%s" % m_getPopupOrderList)
        # print(m_getPopupOrderList)
        # print(orderCode)

        # 设置支付密码
        # pay_password=e10adc3949ba59abbe56e057f20f883e   //------123456-------
        url_setPayPwd = "http://39.108.195.82:8080/flyapi/paypwd/set?version=1.0&terminal=1"
        setPayPwd_data = {"pay_password": 'e10adc3949ba59abbe56e057f20f883e'}
        setPayPwd = session.post(url_setPayPwd, data=setPayPwd_data)
        # print(setPayPwd.text)

        # 验证支付密码
        url_givePayPwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
        givePayPwd = session.get(url_givePayPwd, data='')
        m_givePayPwd = givePayPwd.json()
        # print(givePayPwd.text)

        # POST http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0 #支付订单
        url_payPwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
        payPwd_data = {'orderCode': '%s' % payPwd_orderCode[0], "password": 'e10adc3949ba59abbe56e057f20f883e'}
        payPwd = session.post(url_payPwd, data=payPwd_data)
        print('%s付款成功' % phone)


def gm1():
    # 登陆
    f = r'C:\\Users\\Administrator\\Desktop\\login_getMoney.txt'  # 你所要打开的特定目录的特定文件
    phone = open(f, 'r').readlines()  # 把文件中的每一行作为一个元素添加到列表phone上
    # skuId = '86ee6fef41114e439532f19c75558072'  # 购买商品的skuId ##店主礼包
    skuId = '2298d4318d7c4d1783384fdb43711fe5'   #普通商品
    session = requests.Session()  # 存储cookies

    # 迭代txt文件的phone
    for phonea in phone:
        phone = phonea.strip('\n')
        session = requests.Session()  # 存储cookies
        url_login_test = "http://39.108.195.82:8080/flyapi/login?version=1.0"  # 用户登陆
        test_login_data = {'username': phone, "password": 'e10adc3949ba59abbe56e057f20f883e', "origin": '1'}
        login = session.post(url_login_test, data=test_login_data)  # 用post请求获得session
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

        # 获取收货地址(写一个判断没有再添加收货地址)△怎么获得未加密的cookies，以字典代入
        url_getAddress = "http://39.108.195.82:8080/flyapi/address/list?pageOffset=1&version=1.0"
        getAddress = session.get(url_getAddress, data='')
        userAddress = getAddress.json()
        address = re.findall(r"addressId': '(.*?)'", "%s" % userAddress)
        addressId = address[0]
        quantity = '1'
        # 生成订单
        url_add = "http://39.108.195.82:8080/flyapi/order/add?version=1.0"
        # 普通产品
        add_data = '{"orderFrom":1,"couponId":"","remark":"","products":[{"skuId":"%s","quantity":%s}],' \
                  '"addressId":"%s"}' % (skuId, quantity, addressId)
        add = session.post(url_add, data=add_data)
        print(add.json())
        payPwd_orderCode = re.findall(r"orderCode\":\"(.*?)\"", "%s" % add.text)
        # 获取待支付订单列表
        url_getPopupOrderList = "http://39.108.195.82:8080/flyapi/popupOrder/" \
                                "getPopupOrderList?pageOffset=1&pageSize=10&version=1.0"
        getPopupOrderList = session.get(url_getPopupOrderList, data='')
        m_getPopupOrderList = getPopupOrderList.json()
        re.findall(r"orderCode\': \'(.*?)'", "%s" % m_getPopupOrderList)
        # 验证支付密码
        url_givePayPwd = "http://39.108.195.82:8080/flyapi/paypwd/confirm?pay_" \
                         "password=e10adc3949ba59abbe56e057f20f883e&version=1.0&terminal=1"
        givePayPwd = session.get(url_givePayPwd, data='')
        givePayPwd.json()

        url_payPwd = "http://39.108.195.82:8080/flyapi/order/payPwd?version=1.0&terminal=1"
        payPwd_data = {'orderCode': '%s' % payPwd_orderCode[0], "password": 'e10adc3949ba59abbe56e057f20f883e'}
        session.post(url_payPwd, data=payPwd_data)
        print('%s付款成功' % phone)


if __name__ == '__main__':
    gm()
    # jq()
    # a = input('注册按1，加钱按2，购买产品按3，一条龙按4：')
    # if a == '1':
    #     zc()
    # elif a == '2':
    #     jq()
    # elif a == '4':
    #     zc()
    #     jq()
    #     gm1()




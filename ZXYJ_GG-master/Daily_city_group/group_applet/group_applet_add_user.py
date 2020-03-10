#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25/025 19:49
# @Author  : 刘登攀
# @Site    : 
# @File    : group_applet_add_user.py
# @Software: PyCharm
import requests
import threading
import xlrd


def add_user(phone):
    for i in range(2796, len(phone)):
        session = requests.session()
        headers = {'ContentType': "application/json"}
        url = 'http://192.168.1.8:8080/groupApi/user/add?phone=%s&password=e10adc3949ba59abbe56e057f20f883e&nickName=thename&userName=name&identityCard' \
              '=86288802542027846&wechatOpenId=&wechat=bin_luyck&wechatUnionId=100SDASAD03ASDSA1587&invitationCode=100042742&version=1.0' % phone[i]
        add_user = session.put(url, headers=headers).json()
        # print(add_user)
        if add_user['message'] == '操作成功':
            print(phone[i], '注册"成功"第%s个' % i)
        else:
            print(phone[i], '注册失败第%s个' % i)


def add_money(phone):
    session = requests.session()
    # 登陆后台
    ht_log_url = 'https://web.zxyjsc.com/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'lzc',
                   'password': '123456'}
    ht_log = session.post(ht_log_url, ht_log_data).json()
    # print(ht_log)

    for i in range(len(phone)):
        # 筛选加钱用户
        get_user_url = 'https://web.zxyjsc.com/groupWebApi/member/list?keys=%s&pageOffset=1&pageSize=10&version=1.0' % phone[i]
        get_user = session.get(get_user_url).json()
        member_id = get_user['data']['datas'][0]['memberId']
        print(member_id)

        # 提交加钱申请
        add_money_url = 'https://web.zxyjsc.com/groupWebApi/member/addChangeExamine'
        add_money_data = {'memberId': member_id,
                          'type': '1',
                          'moneyStr': '9000',
                          'remark': 'jq',
                          'changeType': '0',
                          'version': '1.0'}
        a = session.post(add_money_url, add_money_data).json()
        print(a['message'])

        # 筛选加钱审核记录
        get_add_money_url = 'https://web.zxyjsc.com/groupWebApi/memberChange/getChangeExamine?' \
                            'phone=%s&type=&status=&startDate=&endDate=&updateStartDate=&updateEndDate=&pageOffset=1&pageSize=10&version=1.0&terminal=3' % phone[i]
        get_add_money = session.get(get_add_money_url).json()
        change_examine_id = get_add_money['data']['datas'][0]['changeExamineId']

        # 同意审核
        consent_add_money_url = 'https://web.zxyjsc.com/groupWebApi/memberChange/auditChangeExamine?version=1.0&terminal=3'
        consent_add_money_data = {'changeExamineIds': change_examine_id,
                                  'status': '1'}
        mesg = session.post(consent_add_money_url, consent_add_money_data).json()
        print(phone, mesg['message'])


# 读取excl表
def excl():
    open_excl = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\add_user.xls')
    data_sheet = open_excl.sheets()[0]
    rownum = data_sheet.nrows
    colnum = data_sheet.ncols

    phone = []
    for i in range(1, rownum):
        for j in range(colnum):
            phone.append(int(data_sheet.cell(i, j).value))


if __name__ == '__main__':
    open_excl = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\add_user.csv')
    data_sheet = open_excl.sheets()[0]
    rownum = data_sheet.nrows
    colnum = data_sheet.ncols

    phone = []
    for i in range(1, rownum):
        for j in range(colnum):
            phone.append(int(data_sheet.cell(i, j).value))
    add_user(phone)
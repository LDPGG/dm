#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22/022 14:34
# @Author  : 刘登攀
# @Site    : 
# @File    : group_add_money.py
# @Software: PyCharm
import requests
from Daily_city_group.group_port import ttttttt


# 加钱
def add_money(phone, money, wechatOpenId, invitationCode):
    session = requests.session()
    # 创建账号
    # ttttttt.sign_in(phone, wechatOpenId, invitationCode)

    # 登陆后台
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'yg',
                   'password': 'e10adc3949ba59abbe56e057f20f883e'}
    ht_log = session.post(ht_log_url, ht_log_data).json()
    # print(ht_log)

    # 筛选加钱用户
    get_user_url = 'http://39.108.195.82:8080/groupWebApi/member/list?keys=%s&pageOffset=1&pageSize=10&version=1.0' % phone
    get_user = session.get(get_user_url).json()
    member_id = get_user['data']['datas'][0]['memberId']
    print(member_id)

    # 提交加钱申请
    add_money_url = 'http://39.108.195.82:8080/groupWebApi/member/addChangeExamine'
    add_money_data = {'memberId': member_id,
                      'type': '1',
                      'moneyStr': money,
                      'remark': 'jq',
                      'changeType': '0',
                      'version': '1.0'}
    a = session.post(add_money_url, add_money_data).json()
    print(a['message'])

    # 筛选加钱审核记录
    get_add_money_url = 'http://39.108.195.82:8080/groupWebApi/memberChange/getChangeExamine?' \
                        'phone=%s&type=&status=&startDate=&endDate=&updateStartDate=&updateEndDate=&pageOffset=1&pageSize=10&version=1.0&terminal=3' % phone
    get_add_money = session.get(get_add_money_url).json()
    change_examine_id = get_add_money['data']['datas'][0]['changeExamineId']

    # 同意审核
    consent_add_money_url = 'http://39.108.195.82:8080/groupWebApi/memberChange/auditChangeExamine?version=1.0&terminal=3'
    consent_add_money_data = {'changeExamineIds': change_examine_id,
                              'status': '1'}
    mesg = session.post(consent_add_money_url, consent_add_money_data).json()
    print(phone, mesg['message'])


if __name__ == '__main__':
    phone = '15386174586'
    money = '90000'
    wechatOpenId = 'ogLGp5UiGQ70tEqpuSqwUhEWB2hM'
    invitationCode = '100039788'
    add_money(phone, money, wechatOpenId, invitationCode)

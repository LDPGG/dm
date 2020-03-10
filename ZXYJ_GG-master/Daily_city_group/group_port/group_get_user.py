#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14/014 15:11
# @Author  : 刘登攀
# @Site    : 
# @File    : group_get_user.py
# @Software: PyCharm
import requests

session = requests.Session()


# 查询等级
def get_user():
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'yyg',
                   'password': '123456'}
    session.post(ht_log_url, ht_log_data)

    phone = ['15386174586', '15113597820', '18612483433']
    for i in phone:
        url = 'http://39.108.195.82:8080/groupWebApi/member/list?keys=%s&pageOffset=1&pageSize=10&version=1.0' % i
        user = session.get(url).json()
        print(i + ':' + user['data']['datas'][0]['memberTypeStr'])

        # jf_url = 'http://39.108.195.82:8080/groupWebApi/score/list/get?keys=%s&version=1.0' % i
        # jf = session.get(jf_url).json()
        # print('当前积分：', jf['data']['datas'][0]['totalScore'])


# 修改等级
def set_lv():
    ht_log_url = 'http://39.108.195.82:8080/groupWebApi/login?version=1.0&terminal=3'
    ht_log_data = {'username': 'yyg',
                   'password': '123456'}
    session.post(ht_log_url, ht_log_data)

    i = ['15386174586']  # 下单账户
    # i = ['15113597820']  # 一级
    # i = ['18612483433']  # 二级

    url = 'http://39.108.195.82:8080/groupWebApi/member/list?keys=%s&pageOffset=1&pageSize=10&version=1.0' % i[0]
    user = session.get(url).json()
    member_id = user['data']['datas'][0]['memberId']

    set_rank_url = 'http://39.108.195.82:8080/groupWebApi/member/updateMemberGrade?'
    set_rank_data = {'memberId': member_id,
                     'newMemberGrade': '1',
                     'oldMemberGrade': '2',
                     'type': '1',
                     'remark': 'tt',
                     'version': '1.0'}
    rank = session.post(set_rank_url, set_rank_data).json()
    print(rank['message'])
    get_user()


if __name__ == '__main__':
    set_lv()
    # get_user()
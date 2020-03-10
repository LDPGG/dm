#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24/024 17:53
# @Author  : 刘登攀
# @Site    : 
# @File    : group_add_user.py
# @Software: PyCharm
import requests
import xlrd
import hashlib

'''
自动注册后台账户
'''

# def a():
#     session = requests.session()
#     login_url = 'https://web.zxyjsc.com/groupWebApi/login?version=1.0&terminal=3'
#     login_data = {'username': 'lzc',
#                   'password': 'e10adc3949ba59abbe56e057f20f883e'}
#     login = session.post(login_url, login_data).json()
#
#     url = 'https://web.zxyjsc.com/groupWebApi/role/get/roleList?version=1.0'
#     a = session.get(url).json()
#     print(a)


def add_user(account, role_id, phone):
    session = requests.session()

    login_url = 'https://web.zxyjsc.com/groupWebApi/login?version=1.0&terminal=3'
    login_data = {'username': 'lzc',
                  'password': 'e10adc3949ba59abbe56e057f20f883e'}
    login = session.post(login_url, login_data).json()
    print(login['message'])

    for i in range(1, len(account)):
        # print(account[i], roleId[i], phone[i], password[i])
        # 添加账户接口
        url = 'https://web.zxyjsc.com/groupWebApi/sysUser/add?' \
              'account=%s&password=e10adc3949ba59abbe56e057f20f883e&roleId=%s&userName=%s&status=0&phone=%s&userType=0&version=1.0' % (account[i], role_id[i], account[i], phone[i])
        # print(url)
        a = session.put(url).json()
        if a['message'] == '操作失败':
            print(account[i]+'的账户已经注册后台账户')
        elif a['message'] == '手机号码已绑定，请更换手机号':
            print(account[i]+'手机号已被使用')
        else:
            print(account[i]+'的'+a['message'])


if __name__ == '__main__':
    # excl路径
    open_excl = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\user.xls')
    # 确定读取的sheet
    data_sheet = open_excl.sheets()[0]
    # 获取sheet行数
    rowNum = data_sheet.nrows
    # 获取sheet列数
    colnum = data_sheet.ncols

    m = hashlib.md5()

    account = ['']  # 姓名
    roleId = ['']   # 权限
    phone = ['']    # 手机号
    # pwd = ['']  # 密码
    for i in range(1, rowNum):
        for j in range(0, colnum):
            # 取姓名
            if j == 0:
                account.append(data_sheet.cell(i, j).value)
            # 取权限
            elif j == 1:
                roleId.append(int(data_sheet.cell(i, j).value))
            # 取手机号
            elif j == 2:
                phone.append(int(data_sheet.cell(i, j).value))
            # # 取密码
            # else:
            #     pswd = data_sheet.cell(i, j).value
            #     b = bytes(pswd, encoding='UTF-8')
            #     m.update(b)
            #     pwd.append(m.hexdigest())
    add_user(account, roleId, phone)

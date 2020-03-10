# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 上午 11:55
# @Author  : 刘登攀阿！！
# @FileName: ceshi.py
# @Software: PyCharm
import requests
import time

def Look():
    url = 'C:\\Users\Administrator\Desktop\\login_getMoney.txt'
    txt = open(url).readlines()
    for phone in txt:
        ph = phone.replace('\n', '')
        # 存储cookies
        session = requests.Session()
        # 登录
        post_url = 'http://39.108.195.48:8080/flyweb/user/login'
        post_login = {'username': 'admin', 'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
        session.post(post_url, data=post_login)

        url_look = 'http://39.108.195.48:8080/flyweb/member/queryMemberList?pager.offset=0&pager.size=10'
        url_look_login = {'keys': ph, 'grade': '99'}
        url_look_like = session.post(url_look, data=url_look_login)
        aa = url_look_like.json()
        profitSumMoney = aa['data']['datas'][0]['profitSumMoney']
        availableMoney = aa['data']['datas'][0]['availableMoney']
        meSumMoney = aa['data']['datas'][0]['meSumMoney']
        firstLevelSumMoney = aa['data']['datas'][0]['firstLevelSumMoney']
        totalSumMoney = aa['data']['datas'][0]['totalSumMoney']
        print('用户%s的当前收益总金额：%s,'
              '零钱：%s,'
              '个人销售金额：%s,'
              '大众家人：%s,'
              '团队销售金额：%s' %(ph,
                                  profitSumMoney/100,
                                  availableMoney/100,
                                  meSumMoney/100,
                                  firstLevelSumMoney/100,
                                  totalSumMoney/100))


        # look_json = url_look_like.json()
        # print(look_json)
        # 收益金额          零钱              个人销售金额          大众家人            团队销售金额
        # profitSumMoney   availableMoney      meSumMoney        firstLevelSumMoney  totalSumMoney
    time.sleep(120)

if __name__ == '__main__':
    Look()
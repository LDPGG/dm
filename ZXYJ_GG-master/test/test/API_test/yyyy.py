import requests
import json
import re

'''
確認收貨腳本
'''

def gm1():
    # 记事本路径
    path = r'C:\\Users\Administrator\Desktop\\login_getMoney.txt'
    # 读取记事本内容
    phones = open(path, 'r').readlines()

    for phone in phones:
        p=phone.replace('\n', '')
        # 存储cookies
        session = requests.Session()
        # 用户登录
        url_login = 'http://39.108.195.82:8080/flyapi/login?version=1.0'
        post_login = {'username': p, "password": 'dc483e80a7a0bd9ef71d8cf973673924', "origin": '1'}
        aa = session.post(url_login, data=post_login)
        # print(aa.json())

        # 獲取已發貨的訂單列表
        url_deliver = 'http://39.108.195.82:8080/flyapi/order/list/search?keyword=&status=3&' \
                      'pageOffset=1&pageSize=15&version=1.0&terminal=1'
        gettake = session.get(url_deliver)
        # print(gettake.json())
        g_gettake = gettake.json()
        orderCode = re.findall("orderCode\': \'(.*?)'", "%s" % g_gettake)
        # print(orderCode)

        # # 確認收貨
        url_take = 'http://39.108.195.82:8080/flyapi/order/received?version=1.0&terminal=1'
        # orderCode=2301539555106427
        try:
            post_take = {'orderCode': orderCode[0]}
            oo = session.post(url_take, data=post_take)
            oo_url = oo.json()
            post_login_oo = re.findall("'message': '订单已确认收货'", "%s" % oo_url)
            print('%s的订单%s%s'%(phone, orderCode[0],post_login_oo))
        except:
            print(phone+'未找到已發貨訂單')
            continue


if __name__ == '__main__':
    gm1()



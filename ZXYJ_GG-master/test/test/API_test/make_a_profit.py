import requests
import json
import xlwt
import re

f = r'C:\\Users\\Administrator\\Desktop\\phone_z1.txt'    #你所要打开的特定目录的特定文件
with open(f, 'r') as file:
    l1 = file.readlines()             #把文件中的每一行作为一个元素添加到列表l1上
# print(l1)                          #假设你要读取第三行打印输出

for phone in l1:
    url_test = "http://39.108.195.48:8080/flyweb/member/queryMemberList?pager.offset=0&pager.size=10"
    test_data={'keys': phone, "inviteCode": '', "isStore": '', 'memberType': "99"}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8d',
        'cookie': "JSESSIONID=552896849A9B73918FD36997B4CBB622"}
# 上面填入jmeter抓到的cookie
    response = requests.post(url_test, data=test_data, headers=header)
    # print(response)
    # print(response.text)
    read = json.loads(response.text)
    en = (read['data']['datas'])
    # DATA = [('手机号', '用户等级', '上级手机号', '零钱', '收益金额', '个人销售金额', '大众家人销售金额', '团队销售金额')]
    # DATA = []
    # print(DATA)
    # a = []
    # print(en)
    for i in en:
        # a += a
        # c = len(en)
        # print(i)
        if i['phone'] not in ['13556119127']:#过滤盛旺的手机号
            a1 = i['phone']
            a7 = i['memberTypeStr']
            a8 = i['referrerPhone']
            a9 = i['gradeStr']
            a2 = i['profitSumMoney'] / 100
            a3 = i['availableMoney'] / 100
            a4 = i['meSumMoney'] / 100
            a5 = i['firstLevelSumMoney'] / 100
            a6 = i['totalSumMoney'] / 100
            a = [a1, '—' + a7, a9, '收益', '%s' % (a2), '   ', '个人', a4, '家人', a5, '团队', a6, '个人家人总和', a4+a5] #'———' + a8,  '零钱', a3, '会员等级',
            print(a)
    # print(read)


        # print('('+a1+')')
        #for b in a:
         #   c = print(b)
            # for c in b:S
            #     d = [(c)]
            #     print(d)





        # if en != '{"code":0,"message":"success","data":{"datas":[],"pageOffset":0,"pageSize":10,"totalRecord":0,"totalPage":0,"ex":{}}}':
        #
        #
        # print(a)


    # workbook = xlwt.Workbook(encoding='utf-8')
    # booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    # for a, row in enumerate(DATA):
    #     for j, col in enumerate(row):
    #         booksheet.write(a, j, col)
    #     # # DATA = (('手机号', '收益金额', '零钱', '个人销售金额', '大众家人销售金额', '团队销售金额'),
    #     # #         (a1, a2, a3, a4, a5, a6)
    #     # #         )
    #     #
    # workbook.save(r'C:\Users\duan\Desktop\grade.xls')
    # read = response.json()
    # read = json.dumps(res_value, sort_keys=True, ensure_ascii=False, indent=4)
    # print(read)
    # print(re.findall(r'"phone":"(.+?)"', sresponse.text)








        # url_login, url_test = "http://39.108.195.48:8080/flyweb/user/login","http://39.108.195.48:8080/flyweb/member/queryMemberList?pager.offset=0&pager.size=10"
# login_data = {'username': 'admin', 'passwd': 'e10adc3949ba59abbe56e057f20f883e'}
#
# r = requests.post(url_login, data=login_data)
# _cookies = r.cookies
# test_data={'keys': '19911111101', "inviteCode": '', "isStore": '', 'memberType':"99"}
# # print(_cookies)
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#     'Accept-Encoding': 'gzip, deflate',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8d',
#     'cookie': 'cookies=_cookies'# （请求中的cookie，抓包获取的）
# }
# response = requests.post(url_test, data=test_data, headers=header)
# print(response.text)













# r = requests.get(url_test, cookies=_cookies,data=test_data)

# res_value=r.json()
#
# d1 = json.dumps(res_value,sort_keys=True,ensure_ascii=False,indent=4)
# print u'返回结果：'
# print d1










# def login():
#     print "正在请求登录页面..."
#     login_page_url = "登录页面的的url"
#     login_html = s.get(login_page_url)
#     print "正在解析"
#     post_key = get_post_key(login_html.text)
#
#     login_url = "登录url"
#     name, password = get_account()
#     login_data = s.post(url=login_url, data={
#         "name": name,
#         "password": password,
#         "post_key": post_key
#     })
#     print login_data.text
#
# if __name__ == '__main__':
#     with requests.Session() as s:
#         login()
#
# 作者：Luck
# 链接：https://www.zhihu.com/question/45872828/answer/156012837
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





# # -*- coding: UTF-8 -*-
# from urllib import request
# from http import cookiejar
#
# if __name__ == '__main__':
#     #声明一个CookieJar对象实例来保存cookie
#     cookie = cookiejar.CookieJar()
#     #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler=request.HTTPCookieProcessor(cookie)
#     #通过CookieHandler创建opener
#     opener = request.build_opener(handler)
#     #此处的open方法打开网页
#     response = opener.open('http://39.108.195.48:8080/flyweb/user/login')
#     #打印cookie信息
#     for item in cookie:
#         print('Name = %s' % item.name)
#         print('Value = %s' % item.value)
#
#
#



# import requests
# import json
#
# s = requests.Session()
# def test_qualification_add():
#     url = "http://39.108.195.48:8080/flyweb/user/login"  # 测试的接口url
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     data = dict(username="admin", passwd=u'e10adc3949ba59abbe56e057f20f883e')
#     r = requests.post(url=url, headers=headers, json=data)  # 发送请求
#     # return r.json
#     # print(r)
#     print(r.text)  # 获取响应报文
#     print(r.status_code)
#
#
# if __name__ == "__main__":
#     test_qualification_add()




# ====================================================



# def mylogin():
#     # 登录用如下这个接口
#     url_login = 'http://39.108.195.48:8080/flyweb/user/login'
#
#     # 自定义请求头
#     header_login ={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#                 'X-Requested-With': 'XMLHttpRequest',
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#                 'Content-Type': 'application/x-www-form-urlencoded',
#                 'Referer': 'http://39.108.195.48:8080/flyweb/user/login',
#                 'Accept-Encoding': 'gzip, deflate',
#                 'Accept-Language': 'zh-CN,zh;q=0.9',
#                 'Cookie': 'JSESSIONID=DD9B749D7BE1CA3BC15F7C0E83D47D31; JSESSIONID=FD38BBF22C8F4D66393821'
#                          '8A16AA0FEB; cartcount_isview=true; cartCheckList=401969; _'
#                          'ga=GA1.2.198003739.1475039942; _gat=1; Hm_lvt_6b905'
#                          'f228492484ca5d757ea626ddfbd=1474373126,1474519323,1474861167,1474874008; Hm_lpvt_6b905'
#                          'f228492484ca5d757ea626ddfbd=1475039942'}
#
# # 访问登录页面
# data_login = {'loginAccount':'sunyang@163.com', 'password':'111111', 'rememberMe':1}
# userlogin = requests.post(url_login, data=data_login, headers=header_login)
# print(userlogin.url)
# ''' 当只输出response时，返回的是状态码：<Response [200]>'''
# print (userlogin)
# # 输出json格式的返回值
# pprint(userlogin.json())
#
#
# def mylogin():
#     # 登录用如下这个接口
#     url_login = 'http://www.cmall.com/memberSite/sso/loginForOutsideJson'
#
#     # 自定义请求头
#     header_login ={'Accept': 'application/json, text/javascript, */*; q=0.01',
#                    'Origin': 'http://www.cmall.com', 'X-Requested-With': 'XMLHttpRequest',
#                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
#                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#                    'Referer': 'http://www.cmall.com/login.new.html',
#                    'Accept-Encoding': 'gzip, deflate',
#                    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
#                    'Cookie': 'JSESSIONID=DD9B749D7BE1CA3BC15F7C0E83D47D31; JSESSIONID=FD38BBF22C8F4D663938218A16AA0FEB; '
#                              'cartcount_isview=true; cartCheckList=401969; _ga=GA1.2.198003739.1475039942; '
#                              'gat=1; Hm_lvt_6b905f228492484ca5d757ea626ddfbd=1474373126,1474519323,1474861167,1474874008; Hm_lpvt_6b905f228492484ca5d757ea626ddfbd=1475039942'}
#
#     # 访问登录页面
#     data_login = {'loginAccount':'sunyang@163.com', 'password':'111111', 'rememberMe':1}
#     userlogin = requests.post(url_login, data=data_login, headers=header_login)
#     print(userlogin.url)
#     ''' 当只输出response时，返回的是状态码：<Response [200]>'''
#     print (userlogin)
#     # 输出json格式的返回值
#     pprint(userlogin.json())
#     return userlogin.cookies
#
# cookies = mylogin()
# requests.post(url,data,cookies)
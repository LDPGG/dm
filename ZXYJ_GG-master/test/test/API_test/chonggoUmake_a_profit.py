import requests
import json
import xlwt
import re

f = r'C:\\Users\\duan\\Desktop\\phone_z1.txt'    #你所要打开的特定目录的特定文件
l2 = []
with open(f, 'r') as file:
    l1 = file.readlines()             #把文件中的每一行作为一个元素添加到列表l1上
# print(l1)                          #假设你要读取第三行打印输出
for phone in l1:
    url_test = "http://39.108.195.48:8080/flyweb/member/queryMemberList?pager.offset=0&pager.size=10"
    test_data={'keys': phone, "inviteCode": '', "isStore": '', 'memberType':"99"}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8d',
        'cookie': "JSESSIONID=26EF986259F43844D9201DC9C58AF469"}
# 上面填入jmeter抓到的cookie
    response = requests.post(url_test, data=test_data, headers=header)

    # print(response.text)
    read = json.loads(response.text)
    l2.append(read['data']['datas'])
# print(l2)
l3 = []
for a in l2:
    a1 = a[0]['phone']
    a7 = a[0]['memberTypeStr']
    a8 = a[0]['referrerPhone']
    a2 = a[0]['profitSumMoney'] / 100
    a3 = a[0]['availableMoney'] / 100
    a4 = a[0]['meSumMoney'] / 100
    a5 = a[0]['firstLevelSumMoney'] / 100
    a6 = a[0]['totalSumMoney'] / 100
    # i = [a1, '———' + a7, '———' + a8, '———', a2, '———', a3, '———', a4, '———', a5, '———', a6]
    i = [a1, a7, a8, a2, a3, a4, a5, a6]
    l3.append(i)
print(l3)
# 打印到excel
# DATA = [('手机号', '用户等级', '上级手机号', '收益金额', '零钱', '个人销售金额', '大众家人销售金额', '团队销售金额')]
workbook=xlwt.Workbook(encoding='utf-8')
booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
DATA = [['手机号', '用户等级', '上级手机号', '收益金额', '零钱', '个人销售金额', '大众家人销售金额', '团队销售金额']]+ l3
# print(DATA)
for i,row in enumerate(DATA):
    for j,col in enumerate(row):
        booksheet.write(i,j,col)
workbook.save(r'C:\Users\duan\Desktop\grade.xls')


    # DATA = [('手机号', '用户等级', '上级手机号', '收益金额', '零钱', '个人销售金额', '大众家人销售金额', '团队销售金额')]
    # DATA = []
    # print(DATA)
    # a = []
    # for i in en:
    #     a += a
    #     # c = len(en)
    #     a1 = i['phone']
    #     a7 = i['memberTypeStr']
    #     a8 = i['referrerPhone']
    #     a2 = i['profitSumMoney'] / 100
    #     a3 = i['availableMoney'] / 100
    #     a4 = i['meSumMoney'] / 100
    #     a5 = i['firstLevelSumMoney'] / 100
    #     a6 = i['totalSumMoney'] / 100
    #     a = [a1, '———' + a7, '———' + a8, '———', a2, '———', a3, '———', a4, '———', a5, '———', a6]
    #     print(a)

# l = [1,2,3,4,5,6,7,8,9]
#
# ll = []                          #定义一个空列表
# for i in l:                      #循环l中的值，每次取一个值给i
#     if i !=3:                    #判断i是否等于3
#         ll.append(i * 10)        #将不等于3的值乘以10，并添加进ll
# print(ll)                        #打印ll结果
#
#
# aa = [((111))]                        #定义一个空列表
# for b in ll:                   #循环ll中的值，每次取一个值给b
#     if b >= 50:                #判断ll中取出的值是否大于50
#         aa.append(b)           #把大于50的值加入到aa列表中
# print(aa)

# a = [('19911111102', 0.0, 10012.0, 0.0, 0.0, 0.0)]
# b = [('19911111108', 0.0, 10012.0, 0.0, 0.0, 0.0)]
# print(a+b)
# import collections
# dic = collections.OrderedDict()
# # dic = dict()
# dic['a'] = 1
# dic['b'] = 2
# dic['c'] = 3
# print("dic is:", dic.items())

# import json
# jsons = json.dumps(dic)
# print("jsons:",jsons)
import requests
import json
import xlwt
import re
url_invitationCode = 'http://39.108.195.82:8080/flyapi/user/getMemberInfoByInviteCode?inviteCode=19922111111&version=1.0'  #查邀请人号
r = requests.get(url_invitationCode, data='', headers='', cookies='')
res_value = r.json()
d1 = json.dumps(res_value,  sort_keys=True, ensure_ascii=False, indent=4)
print(d1)
read = json.loads(r.text)
en = (read['data']['inviteCode'])
print(en)

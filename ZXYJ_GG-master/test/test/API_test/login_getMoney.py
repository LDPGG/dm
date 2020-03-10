import requests
import json
import xlwt
import re
import collections
import requests
import json

# 19922111144，19922111145
# ======================================从文件创建用户字典，以及排序
filepath = r'C:\\Users\\duan\\Desktop\\login_getMoney.txt'    #你所要打开的特定目录的特定文件
def load_dict_from_file(filepath):

    _dict = collections.OrderedDict()
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(':')
                _dict[key] = value
    except IOError as ioerr:
        print("文件 %s 不存在" % (filepath))

    return _dict                      #假设你要读取第三行打印输出
# print(load_dict_from_file(filepath))
# =======================================迭代用户字典
for phone_user, phone_Inv in load_dict_from_file(filepath).items():#怎么迭代的传入多个参数
    # a = 'http://39.108.195.82:8080/flyapi/user/getMemberInfoByInviteCode?inviteCode=%s&version=1.0' % phone_Inv
    # print(a)
    url_invitationCode = 'http://39.108.195.82:8080/flyapi/user/getMemberInfoByInviteCode?inviteCode=%s&version=1.0' % phone_Inv # 查邀请人号
    url_newloginer = "http://39.108.195.82:8080/flyapi/user/add?version=1.0"
    # test_Inv_data = {'inviteCode': '19922111111', 'version': '1.0'}   #这段报错：未知版本号
# ===================================拿inviteCode邀请人号码
    r = requests.get(url_invitationCode, data='', headers='', cookies='')
    res_value = r.json()
    d1 = json.dumps(res_value, sort_keys=True, ensure_ascii=False, indent=4)
    # print(d1)
    read = json.loads(r.text)
    en = (read['data']['inviteCode'])
    print(en)
    # ==================================================批量注册用户
    test_data={'password': 'dc483e80a7a0bd9ef71d8cf973673924', "invitationCode": en, "phone": phone_user, 'checkNumber':"20160920"}
    header = {
        'User-Agent': 'okhttp/3.8.0',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8d',
        'cookie': ""}
# 上面填入jmeter抓到的cookie
    response = requests.post(url_newloginer, data=test_data, headers=header)
    read = json.loads(response.text)
    print(read)
    # =================================================充钱


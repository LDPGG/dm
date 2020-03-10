import requests
import json
import xlwt
import re
import collections
import requests
import json

# 设置限购时间
# ======================================从文件创建用户字典，以及排序
filepath = r'C:\\Users\\duan\\Desktop\\goods_time.txt'    #你所要打开的特定目录的特定文件
def load_dict_from_file(filepath):

    _dict = collections.OrderedDict()
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split('/')
                _dict[key] = value
    except IOError as ioerr:
        print
        "文件 %s 不存在" % (filepath)

    return _dict                      #假设你要读取第三行打印输出
# print(load_dict_from_file(filepath))
# =======================================迭代用户字典
for startTime, endTime in load_dict_from_file(filepath).items():#怎么迭代的传入多个参数
    # a = 'http://39.108.195.82:8080/flyapi/user/getMemberInfoByInviteCode?inviteCode=%s&version=1.0' % phone_Inv
    # print(a)
    url_saveSku = 'http://39.108.195.48:8080/flyweb/product/saveSku'
    # ==================================================批量注册用户
    test_data = {'skuId': '62111799632a4669ac2731d6d899d158', "skuName": '五色口红压盘',
                 "skuCode": 'SG741', 'barCode': "1568419644+61",
                 'stock': "974", 'costPriceStr': "25.00",
                 'retailPriceStr': "32.90",'marketPriceStr': "128.00",
                 'platformProfitStr': "5.00", 'weight': "50",
                 'saleCount': "72", 'buyScore': "32",
                 'quantity': "0", 'buyMinQuantity': "2",
                 'buyMaxQuantity': "6", 'intro': "温馨提示：西藏，内蒙，甘肃，新疆，宁夏，青海不包邮敬请谅解，纯手工制作，无任何添加剂，孕妇可用，保湿滋润持久不掉色，（大品牌口红代替色）",
                 'distributionProfitStr': "1.88", 'firstProfitStr': "0.94",
                 'secondProfitStr': "0.56", 'threeProfitStr': "0.37",
                 'startTime': startTime, 'endTime': endTime,
                 'loopSize': "0", 'type': "0", 'resType': "0"}
    header = {
        'User-Agent': 'okhttp/3.8.0',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8d',
        'cookie': "JSESSIONID=1D6155280F7FC1BD29E7DF18EE94E3FE"}
# 上面填入jmeter抓到的cookie
    response = requests.post(url_saveSku, data=test_data, headers=header)
    read = json.loads(response.text)
    print(read)
    # =================================================充钱

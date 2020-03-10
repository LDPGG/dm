# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 0023 上午 9:21
# @Author  : 刘登攀阿！！
# @FileName: WXHF.py
# @Software: PyCharm
'''
微信自动回复v1.0
'''
import itchat
import requests


# 登陆微信
itchat.auto_login(hotReload=True)
# 获取好友列表
listFd = itchat.get_friends()


def get_response(message):
    # API调用
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
         'key': '04f44290d4cf462aae8ac563ea7aac16',
         'info': message,
         'userid': 'robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r['text']
    except:
        return


@itchat.msg_register(itchat.content.TEXT)  # 设置回复消息
def tuling_reply(msg):
    # 获取好友消息
    defaultReply = 'QQ:1583141776-好友消息：' + msg['Text']
    print(defaultReply)
    # 获取机器人回复
    reply = get_response(msg['Text'])
    print('QQ:1583141776-机器人回复：' + reply)
    return reply or defaultReply


# 运行
itchat.run()

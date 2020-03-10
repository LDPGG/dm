# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 0023 上午 9:21
# @Author  : 刘登攀阿！！
# @FileName: WXHF.py
# @Software: PyCharm

import itchat
import requests
'''
微信自动回复
'''

# 获取好友列表
listFd = itchat.get_friends()


def get_response(message):
    # 显示好友回复
    print('好友：'+message)
    # API调用
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
         'key': '04f44290d4cf462aae8ac563ea7aac16',
         'info': message,
         'userid': 'robot',
    }
    try:
        # 接收机器人回复消息
        r = requests.post(api_url, data=data).json()
        # 显示机器人回复
        print('机器人：'+r.get('text'))
        return r
    except:
        return


@itchat.msg_register(itchat.content.TEXT)  # 设置回复消息
def tuling_reply(msg):
    return get_response(msg["Text"])["text"]


if __name__ == '__main__':
    # 登陆微信
    itchat.auto_login(hotReload=True)
    # 运行
    itchat.run()

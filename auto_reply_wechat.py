import itchat
import requests
import re
import time
import json
from itchat.content import *


# 监听msg是谁发给我消息
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
# 通过
def text_replay(msg):
    friend = itchat.search_friends(userName=msg['FromUserName'])

    try:
        if msg['Type'] == 'Text':
            resp = qingyun_reply(msg['Text'])
            text = resp.json().get("content")

            print(r'用户名：%s，消息：%s, \n 自动回复内容：%s' % (friend['RemarkName'], msg['Text'], text))

            # itchat.send(r"Friend:%s -- %s  "
            #             r'Time:%s  '
            #             r'Message:%s' % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content))
            itchat.send(text, toUserName=msg['FromUserName'])
            print("----------------------------------------------------------------------------------------")
        else:
            print("不支持的数据类型，不支持自动回复")
            print("----------------------------------------------------------------------------------------")
    except Exception as error:
        print("error:" + error)


def tuling_reply(msg):
    # 
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    message = msg['Text']
    headers = {
        "X-Member-Id": "23832170000",
        "X-Region": "1100000",
        "X-Channel": "01",
        "Content-Type": "application/json;charset=UTF-8"
    }
    print(message)
    data1 = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": message
            }
        },
        "userInfo": {
            "apiKey": "自己的apiKey",
            "userId": "自己的用户号"
        }
    }

    print(data1)
    return requests.post(api_url, headers=headers, data=json.dumps(data1))


def qingyun_reply(msg):
    api_url = 'http://api.qingyunke.com/api.php'
    data = {
        "key": "free",
        "appid": 0,
        "msg": msg
    }

    headers = {'content-type': "application/json"}

    return requests.get(api_url, params=data, headers=headers)


itchat.auto_login()
itchat.run()

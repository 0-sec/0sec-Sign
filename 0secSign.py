# -*- coding:utf-8 -*-

import requests
import base64
import json

base64_image = ''
base64_uuid = ''

#验证码账号密码http://api.ttshitu.com
VcUser = ''
VcPass = ''
#文库账号密码
0secWiikUser = ''
0secWiikPass = ''


# 推送类型
pushType = ''  # telegram|ftpush|bark|enterprise_wechat|dingtalk

# 钉钉推送
DingtalkAccessToken = ''  # 创建webhook机器人时的access_token


# 方糖推送
FTServerKey = ''  # 方糖 Server酱申请的skey

# Telegram推送配置
TelegramToken = ''  # telegram token
TelegramChadId = ''  # telegram token

# Bark推送配置
BarkToken = ''  # Bark Token
BarkServer = ''  # BarkServer

# plus推送配置
PlusPush = ''  # plus push token

# 企业微信推送
EwechatPushToken = ''
EwechatAgentId = ''
EwechatAppSecrets = ''


def get_code_uuid():
    global base64_image, base64_uuid
    code_url = "https://wiki.0-sec.org/api/user/captchaImage"
    code_image = requests.get(code_url)
    json_data = json.loads(code_image.content)
    base64_image = json_data['data']['img']
    base64_uuid = json_data['data']['uuid']


def base64_api():
    global base64_image, base64_uuid
    b64 = base64_image
    data = {"username": VcUser, "password": VcPass, "image": b64}  ##你的验证码api账户，需要去ttshitu.com打码平台注册充值
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        print("验证码识别抽风了，再执行一遍吧")


def login(uuid):
    username = 0secWiikUser  #文库账号
    password = 0secWiikPass  #文库密码
    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
               'Content-Type': 'application/json;charset=UTF-8', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
    url = "https://wiki.0-sec.org/api/user/login"
    login_data = {"account": username, "password": password, "code": base64_api(), "uuid": uuid}  ##字典
    data_json = json.dumps(login_data)  ##转json格式
    logins = requests.post(url=url, headers=headers, data=data_json)
    token = json.loads(logins.content)['data']['token']

    return token


def sign(token):
    headers = {'Zero-Token': token}
    url = "https://wiki.0-sec.org/api/profile"
    old_sign_data_json = requests.get(url=url, headers=headers)
    print(old_sign_data_json.content)
    old_sign_data_credit = json.loads(old_sign_data_json.content)['data']['credit']

    url1 = "https://wiki.0-sec.org/api/front/user/sign"
    requests.post(url=url1, headers=headers)

    new_sign_data_json = requests.get(url=url, headers=headers)
    new_sign_data_credit = json.loads(new_sign_data_json.content)['data']['credit']

    if new_sign_data_credit > old_sign_data_credit:
        print("签到成功，您的当前积分为：", new_sign_data_credit)
        datamsg = "0sec文库签到成功！您的当前积分为：{0}".format(str(new_sign_data_credit))

    else:
        print("兄弟，你已经签到过了，你的积分为：", new_sign_data_credit)
        datamsg = "0sec文库签到失败！您的当前积分为：{0}".format(str(new_sign_data_credit))
    if datamsg:
        if pushType == 'ftpush':
            server_chan_push(FTServerKey, datamsg)
        elif pushType == 'telegram':
            telegram_push(TelegramToken, TelegramChadId,  datamsg)
        elif pushType == 'bark':
            bark_push(BarkToken, BarkServer, datamsg)
        elif pushType == 'push_plus_push':
            push_plus_push(PlusPush, datamsg)
        elif pushType == 'enterprise_wechat':
            wecom_id_push(EwechatPushToken, EwechatAgentId,EwechatAppSecrets,datamsg)
        elif pushType == 'dingtalk':
            dingtalk_push(DingtalkAccessToken,datamsg)


# Server Chan Turbo Push
def server_chan_push(sendkey, text):
    url = "https://sctapi.ftqq.com/%s.send" % sendkey
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    content = {"title": "文库签到", "desp": text}
    ret = requests.post(url, headers=headers, data=content)
    print("ServerChan: " + ret.text)

# 叮叮推送 Push
def dingtalk_push(sendkey,text):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(sendkey)
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": text},}
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(webhook, data=String_textMsg, headers=HEADERS)


# Telegram Bot Push
def telegram_push(token, chat_id, text):
    url = "https://api.telegram.org/bot{0}/sendMessage".format(token)
    data = {
        "chat_id": chat_id,
        "text": text,
    }
    ret = requests.post(url, data=data)
    print("Telegram: " + ret.text)


# Bark Push
def bark_push(bark_key, bark_save, text):
    data = {"title": "文库签到", "body": text}
    headers = {"Content-Type": "application/json;charset=utf-8"}
    url = "https://api.day.app/{0}/?isArchive={1}".format(bark_key, bark_save)
    ret = requests.post(url, json=data, headers=headers)
    print("Bark: " + ret.text)


# PushPlus Push
def push_plus_push(token, text):
    url = "http://www.pushplus.plus/send?token={0}&title={1}&content={2}&template={3}".format(
        token, "文库签到", text, "html"
    )
    ret = requests.get(url)
    print("pushplus: " + ret.text)


# Wecom Push
def wecom_id_push(ww_id, agent_id, app_secrets, msg):
    body = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": agent_id,
        "text": {"content": msg},
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800,
    }
    access_token = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(str(ww_id), app_secrets)
    ).json()["access_token"]
    res = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}".format(access_token),
        data=json.dumps(body),
    )
    ret = res.json()
    if ret["errcode"] != 0:
        print("微信推送配置错误")
    else:
        print("Wecom: " + ret)


def main():
    get_code_uuid()
    tokens = login(base64_uuid)
    sign(tokens)


def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()

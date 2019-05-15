"""
Create by Killer at 2019-04-29 13:41
"""

import json
import requests
from wxpy import *
# 调用图灵机器人API，发送消息并获得机器人的回复

bot = Bot(console_qr=False, cache_path=True)


@bot.register()
def print_message(msg):
    print(msg.text)
    return msg.text

# 定位群
test_group = bot.groups().search('朱老师的小课堂')[0]
# 定位朋友
# sender = test_group.search('微信名')[0]
# # 将朋友的的消息转发到文件传输助手
# @bot.register(test_group)
# def forward_boss_message(msg):
#     if msg.member == sender:
#         msg.forward(bot.file_helper, prefix='朱老师发话了')# 堵塞线程embed()

sender = bot.friends().search("Fors3c")[0]
print(sender)

def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "84dd274b01d3492ebc6c3a315c01f3dc"
    payload = {"key": api_key,"info": text, "userid": "UrDady"}
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[机器人] " + result["text"]

@bot.register(test_group)
def forward_group(msg):
    return auto_reply(msg.text)

@bot.register(sender)
def forward_friend(msg):
    return auto_reply(msg.text)

# 交互模式，阻塞线程 使程序一直运行
embed()

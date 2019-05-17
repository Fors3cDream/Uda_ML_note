"""
Create by Killer at 2019-05-17 14:32
"""
import json
import requests
from pprint import pprint

data = {}

try:
    r = requests.get('https://us.api.battle.net/wow/character/Cenarion%20Circle/Ardy?fields=mounts&locale=en_US&apikey=')
    data = json.load(r.text)
except requests.exceptions.SSLError:
    pass

if len(data.keys()) == 0:
    try:
        print("Open local file!")
        fp = open('mount-data.json', 'r')
    except Exception as e:
        print(str(e))
        print("Open file error!")
    finally:
        data = json.load(fp)

for item in data.items():
    print(item)

for item in data.items():
    pprint(item)
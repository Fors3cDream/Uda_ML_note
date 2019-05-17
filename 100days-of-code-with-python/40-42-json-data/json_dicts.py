"""
Create by Killer at 2019-05-17 14:43
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
        fp = open('mount-data.json', 'r')
    except Exception as e:
        print("Open local file error!")
        exit(0)
    finally:
        data = json.load(fp)

for item in data['mounts']:
    pprint(item)

# only the first level is printed
for item in data['mounts']['collected']:
    pprint(item)

#Prints ALL the data associated with 'collected mounts'.


for item in data['mounts']['collected']:
    pprint(item['name'])

#Prints just the data associated with the 'name' key.


is_flying = []
for mount in data['mounts']['collected']:
    if mount['isFlying']:
        is_flying.append(mount)

#Collects all of the applicable mounts and stores them as a list of dicts

#You can then work with the data as normal:

print(len(is_flying))

for i in is_flying:
    print(i)

for i in is_flying:
    print(i['name'])
"""
Create by Killer at 2019-05-28 14:56
"""
from __future__ import unicode_literals
from urllib import request
from pyquery import PyQuery as pq
import json

blog_url = 'https://www.cnblogs.com/Ray-liang/'

def parse_item(i, e):
    doc = pq(e)
    title = doc('.postTitle>a').text()
    parmerlink = doc('.postTitle>a').attr('href')
    pub_date = doc('.dayTitle').text()
    summary = doc('.postCon').text()
    result = {
        'title':title,
        'parmerlink':parmerlink,
        'pub_date': pub_date,
        'summary': summary
    }
    print(json.dumps(result, ensure_ascii=False))
    return result

with request.urlopen(blog_url) as response:
    body = response.read()
    doc = pq(body)
    items = doc('.forFlow>.day').map(parse_item) # 将 doc('.forFlow>.day')一个一个传入parse_item函数中
    with open('output.json', 'wt') as fp:
        fp.write(json.dumps(items, ensure_ascii=False))
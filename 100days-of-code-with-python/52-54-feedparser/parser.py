"""
Create by Killer at 2019-05-17 15:14
"""

import feedparser

FEED_FILE = 'newreleases.xml'

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(entry.published  + ' - ' + entry.title + " : " + entry.link)

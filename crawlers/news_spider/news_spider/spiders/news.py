# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ..items import NewsSpiderItem

class NewsSpider(XMLFeedSpider):
    name = 'news'
    url = 'http://rss.sina.com.cn/news/world/focus15.xml'
    start_urls = [url]

    def parse_node(self, response, selector):
        item = NewsSpiderItem()
        item['title'] = selector.xpath('title/text()').extract_first()
        print("Title is ", item['title'])
        item['link'] = selector.xpath('link/text()').extract_first()
        item['pub_date'] = selector.xpath('pubDate/text()').extract_first()
        item['desc'] = selector.xpath('description/text()').extract_first()
        return item

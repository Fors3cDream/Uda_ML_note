# -*- coding: utf-8 -*-
import scrapy
import json

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    start_index = 0
    start_urls = [BASE_URL % start_index]

    MAX_DOWNLOAD = 1000
    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))

        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}

        self.start_index += infos['count']

        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD:
            yield scrapy.Request(self.BASE_URL % self.start_index)

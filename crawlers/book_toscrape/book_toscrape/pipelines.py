# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.item import Item
import pymongo

class BookPipeline(object):
    review_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def process_item(self, item, spider):
        rating = item['Review_rating']
        if rating:
            item['Review_rating'] = "%d 星" % self.review_rating_map[rating]
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['Title']
        if name in self.book_set:
            raise DropItem('Duplicate book found: %s' % item)
        self.book_set.add(name)
        return item

class BookToscrapePipeline(object):
    exchange_rate = 8.5309
    def process_item(self, item, spider):
        excel_tax = float(item['Price_excel_tax'][1:]) * self.exchange_rate
        incl_tax = float(item['Price_incl_tax'][1:]) * self.exchange_rate
        tax = float(item['Tax'][1:]) * self.exchange_rate
        item['Price_excel_tax'] = ('￥%.2f' % excel_tax)
        item['Price_incl_tax'] = ('￥%.2f' % incl_tax)
        item['Tax'] = ('￥%.2f' % tax)
        return item

class MongoDBPipeline(object):
    # DB_URI = "mongodb://localhost:27017/"
    # DB_NAME = 'scrapy_data'
    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URI = crawler.settings.get('MONGODB_URI')
        cls.DB_NAME = crawler.settings.get('MONGODB_NAME')
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URI)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item
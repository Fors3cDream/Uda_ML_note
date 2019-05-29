# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


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

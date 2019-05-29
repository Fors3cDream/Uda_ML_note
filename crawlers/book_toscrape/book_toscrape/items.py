# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    Title = scrapy.Field()
    UPC = scrapy.Field()
    Product_Type = scrapy.Field()
    Price_excel_tax = scrapy.Field()
    Price_incl_tax = scrapy.Field()
    Tax = scrapy.Field()
    Availability = scrapy.Field()
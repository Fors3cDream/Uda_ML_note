# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem
from bs4 import BeautifulSoup
import re

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
            book_urls = response.css('div.image_container a::attr(href)').extract()
            if book_urls:
                for url in book_urls:
                    book_url = response.urljoin(url)
                    yield scrapy.Request(book_url, callback=self.parse_book)

            # 使用Selector
            # next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
            # if next_url:
            #     next_url = response.urljoin(next_url)
            #     yield scrapy.Request(next_url, callback=self.parse)

            # 使用LinkExtractor
            le = LinkExtractor(restrict_css='ul.pager li.next')
            links = le.extract_links(response)
            if links:
                next_url = links[0].url
                yield scrapy.Request(next_url, callback=self.parse)

    def parse_book(self, response):
        print("Start to parse book at content")
        book = BookItem()
        html = BeautifulSoup(response.text, 'lxml')
        book['Title'] = html.select('#content_inner > article > div.row > div.col-sm-6.product_main > h1')[0].text
        # infos = html.select('#content_inner > article > table > tr > td')
        # book['UPC'] = infos[0].text

        # book['Product_Type'] = html.select('#content_inner > article > table > tbody > tr:nth-child(1) > td')[0].text
        # book['Price_excel_tax'] = html.select('#content_inner > article > table > tbody > tr:nth-child(1) > td')[0].text
        # book['Price_incl_tax'] = html.select('#content_inner > article > table > tbody > tr:nth-child(1) > td')[0].text
        # book['Tax'] = html.select('#content_inner > article > table > tbody > tr:nth-child(1) > td')[0].text
        # book['Availability'] = html.select('#content_inner > article > table > tbody > tr:nth-child(1) > td')[0].text
        book['Review_rating'] = response.css('#content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')
        re_infos = response.css('#content_inner > article > table > tr > td::text').extract()
        book['UPC'] = re_infos[0]
        book['Product_Type'] = re_infos[1]
        book['Price_excel_tax'] = re_infos[2]
        book['Price_incl_tax'] = re_infos[3]
        book['Tax'] = re_infos[4]
        book['Availability'] = re.findall(".*(\d+) available", re_infos[5])[0]
        book['Review_num'] = re_infos[6]
        yield book
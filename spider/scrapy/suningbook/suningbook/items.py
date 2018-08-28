# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningbookItem(scrapy.Item):
    # define the fields for your item here like:
    second_sort = scrapy.Field()
    three_sort_text = scrapy.Field()
    three_sort_href = scrapy.Field()
    book_author = scrapy.Field()
    book_name = scrapy.Field()
    book_synopsis = scrapy.Field()
    book_img = scrapy.Field()
    book_href = scrapy.Field()
    price = scrapy.Field()




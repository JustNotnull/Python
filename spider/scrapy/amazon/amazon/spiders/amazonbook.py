# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonbookSpider(RedisCrawlSpider):
    name = 'amazonbook'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_top_books_l1?ie=UTF8&node=658390051']
    redis_key = "amazon"

    rules = (
        #大分类
        Rule(LinkExtractor(restrict_xpaths=("//div[@aria-live='polite']/li")), follow=True),
        #小分类
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='left_nav browseBox']/ul/li")), follow=True),
        #小小分类
        # Rule(LinkExtractor(restrict_xpaths=("//div[@aria-live='polite']/li")), follow=True),
        #图书详情
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li")), callback="book_detial"),

        #下一页
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']")), follow=True)

    )

    def book_detial(self, response):
        item = {}
        item["book_name"] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        item["book_author"] = response.xpath("//div[@id='bylineInfo']/span[1]/a/text()").extract_first()
        item["book_date"] = response.xpath("//h1[@id='title']/span[3]/text()").extract_first()
        item["book_price"] = response.xpath("//div[@id='soldByThirdParty']/span[2]/text()").extract_first()
        item["book_publish"] = response.xpath("//b[text()='出版社:']/../text()").extract_first()
        print(item)
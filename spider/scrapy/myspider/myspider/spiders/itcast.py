# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['music.163.com”']
    start_urls = ['http://music.163.com/discover/playlist']

    def parse(self, response):
        # li_list = response.xpath("//div[@class='tea_con']//li")
        # for li in li_list:
        #     item = {}
        #     item["name"] = li.xpath(".//h3/text()").extract_first()
        #     item["title"] = li.xpath(".//h4/text()").extract_first()
        #     # print(item)
        #     # Request, BaseItem, dict or None

            div_list = response.xpath("//ul[@class='m-cvrlst f-cb']/li")
            for div in div_list:
                item={}
                item['title'] =div.xpath(".//a[@class='msk']/@title").extract_first()
                item['href'] =div.xpath(".//a[@class='msk']/@href").extract_first()
                yield item

# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import re

# from suningbook.items import SuningbookItem


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        html_href = response.xpath("//ul[@class='ulwrap']/li")
        for html_list in html_href:
            # item = SuningbookItem()
            item ={}
            item["second_sort"] = html_list.xpath("./div[1]/a/text()").extract_first()
            three_sort = html_list.xpath("./div[2]/a")
            for three_sort_href in three_sort:
                item["three_sort_text"] = three_sort_href.xpath("./text()").extract_first()
                item["three_sort_href"]= three_sort_href.xpath("./@href").extract_first()
                print("*"*100)
                print(item["three_sort_href"])
                print("*" * 100)
                if item["three_sort_href"] is not None:
                    item["three_sort_href"] = 'http://snbook.suning.com' +item["three_sort_href"]
                    yield scrapy.Request(
                        item["three_sort_href"],
                        callback=self.parse_book_list,
                        meta={"item": deepcopy(item)}
                    )

    def parse_book_list(self, response):
        item = deepcopy(response.meta["item"])
        html = response.xpath("//div[@class='filtrate-books list-filtrate-books']/ul/li")
        for li in html:
            item["book_name"] = li.xpath("//div[@class='book-title']/a/@title").extract_first()
            item["book_author"] = li.xpath("//div[@class='book-author']/a/text()").extract_first()
            item["book_synopsis"] = li.xpath("//div[@class='book-descrip c6']/text()").extract_first()
            item["book_img"] = li.xpath("//div[@class='book-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='book-img']//img/@src2").extract_first()
            item["book_href"] = li.xpath(".//div[@class='book-title']/a/@href").extract_first()

            yield scrapy.Request(
                item["book_href"],
                callback=self.price,
                meta={"item": deepcopy(item)}
            )

        page_count = int(re.findall("var pagecount=(.*?);", response.body.decode())[0])
        current_page = int(re.findall("var currentPage=(.*?);", response.body.decode())[0])
        if current_page < page_count:
            next_url = item["three_sort_href"] + "?pageNumber={}&sort=0".format(current_page + 1)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta={"item": response.meta["item"]},

            )


    def price(self, response):
        item = response.meta["item"]
        item["price"] = re.findall("\"bp\":'(.*?)',", response.body.decode())
        item["price"] = item["price"][0] if len(item["price"][0]) > 0 else None
        # print(item)
        yield item



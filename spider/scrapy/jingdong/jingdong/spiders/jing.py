# -*- coding: utf-8 -*-
import scrapy
from  copy import deepcopy
from  jingdong.items import JingdongItem
import json


class JingSpider(scrapy.Spider):
    name = 'jing'
    allowed_domains = ['jd.com','p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        for dt in dt_list:
            # item ={}
            item =JingdongItem()
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            dd_list = dt.xpath("./following-sibling::dd[1]/em")
            for dd in dd_list:
                item["s_cate"] = dd.xpath("./a/text()").extract_first()
                item["s_href"] = dd.xpath("./a/@href").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = "https:"+item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.book_detail_list,
                        meta={"item":deepcopy(item)}
                                                )

    def book_detail_list(self,response):
        item = response.meta["item"]
        li_list =response.xpath("//div[@id='plist']/ul/li")
        for li in li_list:
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='p-img']//img/@data-lazy-img").extract_first()
            item["book_img"] = "https:" +item["book_img"]
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["book_author"] = li.xpath("//span[@class='author_type_1']/a/@title").extract_first()
            item["book_store"] = li.xpath(".//span[@class='p-bi-store']/a/@title").extract_first()
            item["book_date"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first().strip()
            item["book_sku"] = li.xpath("./div/@data-sku").extract_first()
            yield scrapy.Request(
                    url="https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"]) + "&pduid=218396815",
                callback=self.price,
                meta={"item": deepcopy(item)}

                            )
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                url="https:" + next_url,
                callback=self.book_detail_list,
                meta={"item":item}

            )
        print(item)

    def price(self,response):
        item = response.meta["item"]
        item["price"] =json.loads(response.body.decode())[0]["op"]
        print(item)
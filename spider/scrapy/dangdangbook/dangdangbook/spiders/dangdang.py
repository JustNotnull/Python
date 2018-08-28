# -*- coding: utf-8 -*-
import scrapy
from  copy import deepcopy
from scrapy_redis.spiders import RedisSpider
import urllib


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "dangdang"

    def parse(self, response):
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl/dt//text()").extract()
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip()) > 0]
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                # item["m_cate"] = dl.xpath("./dt/text()").extract_first().strip()
                item["m_cate"] = dl.xpath("./dt//text()").extract()
                item["m_cate"] = [i.strip() for i in item["m_cate"] if len(i.strip()) > 0][0]
                dd_list = dl.xpath("./dd/a")
                for dd in dd_list:
                    item["s_cate"] = dd.xpath("./@title").extract_first()
                    item["s_href"] = dd.xpath("./@href").extract_first()
                    # print(item)
                    if item["s_href"] is not  None:

                        yield scrapy.Request(
                            item["s_href"],
                            callback=self.book_list,
                            meta={"item":deepcopy(item)}

                      )
    def book_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='bigimg']/li")
        for li in li_list:
            item["book_img"] =li.xpath("./a[@class='pic']/img/@src").extract_first()
            if item["book_img"] == "images/model/guan/url_none.png":
                item["book_img"] = li.xpath("./a[@class='pic']/img/@data-original").extract_first()
            item["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]/a/text()").extract()
            if item["book_author"] ==[]:
                item["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]/text()").extract()
            item["book_name"] = li.xpath("./a[@class='pic']/@title").extract_first()
            item["book_date"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first()
            item["book_publish"] = li.xpath("./p[@class='search_book_author']/span[3]/a/@title").extract_first()
            item["book_desc"] = li.xpath("./p[@class='detail']/text()").extract_first()
            item["book_price"] = li.xpath("./p[@class='price']/span[@class='search_pre_price']/text()").extract_first()
            print(item)
        next_url = response.xpath("//ul[@name='Fy']/li[@class='next']/a/@href").extract_first()
        if next_url is not None:
            # next_url = urllib.parse.urljion(response.url,next_url)
            next_url ="http://category.dangdang.com" + next_url
            print(next_url)
            yield scrapy.Request(
                url=next_url
                ,callback=self.book_list,
                meta={"item":deepcopy(item)}

            )
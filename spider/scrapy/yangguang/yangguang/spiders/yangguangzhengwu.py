# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem

class YangguangzhengwuSpider(scrapy.Spider):
    name = 'yangguangzhengwu'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    def parse(self, response):
        html = response.xpath("//td[@valign='top']//tr")
        # print(html)


        for html_list in html:
            # item = {}
            item = YangguangItem()
            item["number"] = html_list.xpath(".//td[1]/text()").extract_first()
            item["href"] = html_list.xpath(".//td[2]/a[2]/@href").extract_first()
            item["title"] = html_list.xpath(".//td[2]/a[2]/@title").extract_first()
            item["time"] = html_list.xpath(".//td[last()]/text()").extract_first()
            # print(item)
            yield scrapy.Request(
                                item["href"],
                                callback=self.details,
                                meta={"item":item})

        next_url = html.xpath("//a[text()='>']/@href").extract_first()
        print(next_url)
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    def details(self,response):
        item = response.meta["item"]
        item["html_context"] = response.xpath("//div[@class='c1 text14_2']//text()").extract()
        item["html_img"] = response.xpath("//div[@align='center']//img/@src").extract()
        item["html_img"] = ['http://wz.sun0769.com'+i for i in item["html_img"]]
        print(item)
        yield item

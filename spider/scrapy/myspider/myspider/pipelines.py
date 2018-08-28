# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html





class MyspiderPipeline(object):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def process_item(self, item, spider):
        item["hello"] = "world"
        # print(item)
        return item


class MyspiderPipeline1(object):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def process_item(self, item, spider):
        print(item)
        return item

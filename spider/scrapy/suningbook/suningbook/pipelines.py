# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient


# client = MongoClient()
# collection = client["runoob"]["my"]
class SuningbookPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        self.collection = client["runoob"]["sunning"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        return item

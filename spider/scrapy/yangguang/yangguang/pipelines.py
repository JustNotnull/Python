# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from pymongo import MongoClient


class YangguangPipeline(object):
    def open_spider(self, spider):
        # spider.hello = "world"
        client = MongoClient()
        self.collection = client["runoob"]["test"]

    def process_item(self, item, spider):
        # spider.settings.get("MONGO_HOST")
        item["html_context"] = self.process_content(item["html_context"])
        print(item)
        #
        self.collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s", "", i) for i in content]
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content


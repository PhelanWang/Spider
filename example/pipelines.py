# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import codecs
import json
from scrapy.conf import settings
from pymongo import MongoClient


# 保存到文件data.txt
class ExamplePipeline(object):

    def __init__(self):
        self.file = codecs.open("E:\python-scrapy\example\example\spiders\data.txt", "wb+",encoding="utf-8")

    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        line = i + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

# 保存到MongoDB中
class MongoDBPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT'],
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.count = 1

    def process_item(self, item, spider):
        print 'x%d' % self.count,
        self.count += 1
        self.collection.insert(dict(item))
        return item


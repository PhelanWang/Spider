# -*- coding: utf-8 -*-
import scrapy

from example.items import ExampleItem
from scrapy_redis.spiders import RedisSpider

"""
cdibi_crawler,爬取由master_crawler添加到cdibi_crawler:start_urls队列中的页面的内容
"""

class CdibiSpider(RedisSpider):
    name = "cdibi_crawler"
    redis_key = 'cdibi_crawler:start_urls'

    def __init__(self):
        RedisSpider.__init__(self)
        print("cdibi-crawler-start")
        self.count = 1

    def parse(self, response):
        print 'c%d' % self.count,
        self.count += 1
        news_item = ExampleItem()
        items = response.xpath("//ul[@class='news-list']/li")
        for item in items:
            news_item["news_link"] = item.xpath("a/@href").extract()[0]
            news_item["news_title"] = item.xpath("a/text()").extract()[0]
            news_item["news_time"] = item.xpath("span[@class='time']/text()").extract()[0]
            yield news_item

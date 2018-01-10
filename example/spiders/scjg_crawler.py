# -*- coding: utf-8 -*-
import scrapy

from example.items import ExampleItem
from scrapy_redis.spiders import RedisSpider

"""
scjg_crawler,爬取由master_crawler添加到scjg_crawler:start_urls队列中的页面的内容
"""

class ScjgSpider(RedisSpider):
    name = "scjg_crawler"
    redis_key = 'scjg_crawler:start_urls'

    def __init__(self):
        RedisSpider.__init__(self)
        print("scjg-crawler-start")
        self.count = 1

    def parse(self, response):
        print "s%d" % self.count,
        self.count += 1
        news_item = ExampleItem()
        items = response.xpath("//div[@id='list']/a")
        for item in items:
            news_item["news_link"] = item.xpath("@href").extract()[0]
            news_item["news_title"] = item.xpath("span/text()").extract()[0]
            news_item["news_time"] = item.xpath("font/text()").extract()[0]
            yield news_item

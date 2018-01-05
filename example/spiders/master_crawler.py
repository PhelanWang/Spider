# coding: utf-8
from redis import Redis
from scrapy_redis.spiders import RedisSpider


class MasterSpider(RedisSpider):
    name = "master_crawler"
    redis_key = "master:start_urls"

    def __init__(self, *args, **kwargs):
        RedisSpider.__init__(self)
        print("master-start")
        self.cdibi_host = "http://www.cdibi.org.cn"
        self.scjg_host = "http://www.scjg.gov.cn"
        self.s_count = 1
        self.c_count = 1

    def parse(self, response):
        r = Redis()
        if response.url.find(self.cdibi_host) != -1:
            next_page_link = response.xpath("//ul[@class='pagination']/li[@class='next']/a/@href").extract()[0]
            if next_page_link != []:
                r.lpush("master:start_urls", self.cdibi_host + next_page_link)
                r.lpush("cdibi_crawler:start_urls", self.cdibi_host + next_page_link)
                print 'm-c%d' % self.c_count,
                self.c_count += 1
        elif response.url.find(self.scjg_host) != -1:
            next_page_link = response.xpath('//p[@class="fy"]/a/@href')[-2].extract()
            if next_page_link != []:
                r.lpush("master:start_urls", next_page_link)
                r.lpush("scjg_crawler:start_urls", next_page_link)
                print 'm-s%d' % self.s_count,
                self.s_count += 1


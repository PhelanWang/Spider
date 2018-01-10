# coding: utf-8
from redis import Redis
from scrapy_redis.spiders import RedisSpider

# lpush 'master:start_urls' 'http://www.cdibi.org.cn/article/nlist?id=5pRmv'
# lpush 'master:start_urls' 'http://www.scjg.gov.cn/filelist_1_7.html'

"""
master_crawler,初始化的队列是master:start_urls,爬取上面两个页面的下一页链接,
并将cdibi的下一页添加到队列cdibi_crawler:start_urls和master:start_urls中
将scjg的下一页添加到队列cdibi_crawler:start_urls和master:start_urls中
"""

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
            # 提取cdibi的下一页的链接并添加到队列cdibi_crawler:start_urls中和master:start_urls
            next_page_link = response.xpath("//ul[@class='pagination']/li[@class='next']/a/@href").extract()[0]
            print next_page_link
            if next_page_link != []:
                r.lpush("master:start_urls", self.cdibi_host + next_page_link)
                r.lpush("cdibi_crawler:start_urls", self.cdibi_host + next_page_link)
                print 'm-c%d' % self.c_count,
                self.c_count += 1
        elif response.url.find(self.scjg_host) != -1:
            # 提取scjg的下一页的链接并添加到队列scjg_crawler:start_urls中和master:start_urls
            next_page_link = response.xpath('//p[@class="fy"]/a/@href')[-2].extract()
            print next_page_link
            if next_page_link != []:
                r.lpush("master:start_urls", next_page_link)
                r.lpush("scjg_crawler:start_urls", next_page_link)
                print 'm-s%d' % self.s_count,
                self.s_count += 1


# -*- coding: utf-8 -*-
# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # 'example.pipelines.MongoDBPipeline': 400,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "spider_db"
# MONGODB_COLLECTION = "qr_data"

LOG_LEVEL = 'DEBUG'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SCHEDULER_FLUSH_ON_START = True

REDIS_URL = 'redis://@localhost:6379'
# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ExampleItem(Item):
    # define the fields for your item here like:
    # name = Field()
    news_title = Field()
    news_link = Field()
    news_time = Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name=scrapy.Field()
    Link=scrapy.Field()
    Type=scrapy.Field()
    Num=scrapy.Field()
    Location=scrapy.Field()
    Publishtime=scrapy.Field()



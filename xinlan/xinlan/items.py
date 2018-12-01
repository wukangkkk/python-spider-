# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinlanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #大标题的题目和url
    parent_title=scrapy.Field()
    parent_url=scrapy.Field()

    #小类的题目和url
    sub_title=scrapy.Field()
    sub_url=scrapy.Field()

    #小类的存储路径
    sub_filename=scrapy.Field()

    #小类下的子链接
    son_url=scrapy.Field()

    #文章和标题
    head=scrapy.Field()
    content=scrapy.Field()









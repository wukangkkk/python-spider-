# -*- coding: utf-8 -*-
import scrapy
from doubanTop250.items import Doubantop250Item

class DoubanmovieSpider(scrapy.Spider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]
    offset=0
    url='https://movie.douban.com/top250?start='
    start_urls = (
        url+str(offset),
    )

    def parse(self, response):
        item=Doubantop250Item()
        for each in response.xpath('//div[@class="info"]'):
            # 电影标题
            item['title']=each.xpath('.//span[@class="title"][1]/text()').extract()[0]
            #演员信息
            item['actor']=each.xpath('.//div[@class="bd"]/p[1]').extract()[0]
            #评分
            item['score']=each.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            #电影主题
            item['topic']=each.xpath('.//span[@class="inq"]/text()').extract()[0]

            yield item

        if self.offset<225:
            self.offset+=25
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)

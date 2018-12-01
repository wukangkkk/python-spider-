# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentjobSpider(scrapy.Spider):
    name = "tencentJob"
    allowed_domains = ["tencent.com"]
    url='https://hr.tencent.com/position.php?&start='
    offset=0
    start_urls = [url+str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            #初始化实例对像
            item=TencentItem()
            item['Name'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['Link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['Type'] = each.xpath("./td[2]/text()").extract()[0]
            item['Num'] = each.xpath("./td[3]/text()").extract()[0]
            item['Location'] = each.xpath("./td[4]/text()").extract()[0]
            item['Publishtime']= each.xpath("./td[5]/text()").extract()[0]

            yield item


        if self.offset<1680:
            self.offset+=10
        else:
            raise "工作结束"


        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)






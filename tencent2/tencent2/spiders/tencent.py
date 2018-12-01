# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent2.items import Tencent2Item

class TencentSpider(CrawlSpider):
    name = 'tencentspyder'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']
    #获取符合规则的链接
    page_lx = LinkExtractor(allow=("start=\d+"))
    rules = (
        #获取列表的链接,并依次发请求,并且继续跟进,指定回调函数处理
        Rule(page_lx, callback='parse_item', follow=True),
    )
    #指定的回调函数
    def parse_item(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初始化实例对像
            item = Tencent2Item()
            item['Name'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['Link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['Type'] = each.xpath("./td[2]/text()").extract()[0]
            item['Num'] = each.xpath("./td[3]/text()").extract()[0]
            item['Location'] = each.xpath("./td[4]/text()").extract()[0]
            item['Publishtime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
        #
        # if self.offset < 1680:
        #     self.offset += 10
        # else:
        #     raise "工作结束"
        #
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
        #

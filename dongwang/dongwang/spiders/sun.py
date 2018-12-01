# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongwang.items import DongwangItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4'),process_links = "deal_links",follow=True),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

    def deal_links(self, links):
        for link in links:
            link.url = link.url.replace("?", "&").replace("Type&", "Type?")
            print link.url
        return links

    def parse_item(self, response):
        item=DongwangItem()
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]

        # 文字内容，默认先取出有图片情况下的文字内容列表
        item['content'] = response.xpath('//div[@class="contentext"]/text()').extract()[0]

        item['url'] = response.url

        yield item

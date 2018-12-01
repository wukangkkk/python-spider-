# -*- coding: utf-8 -*-
import scrapy
import os
from xinlan.items import  XinlanItem

class SinaspiderSpider(scrapy.Spider):
    name = "sinaSpider"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = (
        'http://news.sina.com.cn/guide/',
    )

    def parse(self, response):
        items=[]
        #所有大类的标题和url
        parent_title=response.xpath('//div//h3[@class="tit02"]/a/text()').extract()
        parent_url=response.xpath('//div//h3[@class="tit02"]/a/@href').extract()

        #所有小类的标题和url
        sub_title=response.xpath('//ul[@class="list01"]/li/a/text()').extract()
        sub_url=response.xpath('//ul[@class="list01"]/li/a/@href').extract()

        #爬去所有的大类
        for i in range(0,len(parent_title)):
            #制定大类的路径和目录名
            parent_filename="./data/"+parent_title[i]
            #如果目录不存在则创建新的目录
            if (not os.path.exists(parent_filename)):
                os.makedirs(parent_filename)

            #爬去所有的小类
            for j in range(0,len(sub_title)):
                item= XinlanItem()
                #保存大类的标题和url
                item['parent_title']=parent_title[i]
                item['parent_url']=parent_url[i]
                #检查小类的url是否同大类的url的开头,是的话返回true
                if_belong=sub_title[j].startswith(item['parent_title'])
                #如果是本大类则存在本大类的目录下
                if (if_belong):
                    sub_filename=parent_filename+'/'+sub_title[j]
                    #如果目录不存在,创建目录
                    if (not os.path.exists(sub_filename)):
                        os.makedirs(sub_filename)
                    #存储小类标题,url,和filename数据
                        item['sub_title']=sub_title[j]
                        item['sub_url']=sub_url[j]
                        item['sub_filename']=sub_filename
                        items.append(item)


        #发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse
        for each in items:
            yield  scrapy.Request( url = each['sub_url'], meta={'meta_1': each}, callback=self.second_parse)

    # 对于返回的小类的url，再进行递归请求
    def second_parse(self,response):
        #提取每次响应的meat数据
        meta_1=response.meta['meta_1']
        #提取所有的son_url链接
        son_url=response.xpath('//a/@href').extract()
        items= []

        for i in range(0, len(son_url)):
            # 检查每个链接是否以大类url开头、以.shtml结尾，如果是返回True
            if_belong = son_url[i].endswith('.shtml') and son_url[i].startswith(meta_1['parent_url'])
            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if (if_belong):
                item = XinlanItem()
                item['parent_title'] = meta_1['parent_title']
                item['parent_url'] = meta_1['parent_url']
                item['sub_url'] = meta_1['sub_url']
                item['sub_title'] = meta_1['sub_title']
                item['sub_filename'] = meta_1['sub_filename']
                item['son_url'] = son_url[i]
                items.append(item)
                # 发送每个小类下子链接url的Request请求，得到Response后连同包含meta数据 一同交给回调函数 detail_parse 方法处理
        for item in items:
            yield scrapy.Request(url=item['son_url'], meta={'meta_2': item}, callback=self.detail_parse)


            # 数据解析方法，获取文章标题和内容

    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath('//h1[@id=\"main_title\"]/text()')
        content_list = response.xpath('//div[@id=\"artibody\"]/p/text()').extract()

        # 将p标签里的文本内容合并到一起
        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item

















# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyspyderPipeline(object):

    def __init__(self):
        #可选实现,做参数初始化
        #do something
        self.file=open("teacher.json",'wb')
    #process_item 是必需要写的,用来处理item数据
    def process_item(self, item, spider):
        #字典的格式不要忘记
        content=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(content.encode("utf-8"))
        return item
    #可选实现,结束spider
    def close_spider(self,spider):
        self.file.close()



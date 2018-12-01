# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XinlanPipeline(object):
    def process_item(self, item, spider):
        son_url= item['son_url']

        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = son_url[7:-6].replace('/', '_')
        filename += ".txt"

        fp = open(item['sub_filename'] + '/' + filename, 'w')
        fp.write(item['content'])
        fp.close()
        return item

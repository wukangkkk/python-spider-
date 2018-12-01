#coding=utf-8
import scrapy
from mySpyder.items import MyspyderItem

class itcastSpyder(scrapy.Spider):
    name="itcast"
    allowed_domains=["itcast.cn"]
    start_urls=("http://www.itcast.cn/channel/teacher.shtml#",)
    def parse(self, response):
        #filename = "teacher.html"
        #open(filename, 'w').write(response.body)
        #items=[]

        for each in response.xpath("//div[@class='li_txt']"):
            #将我们得到的数据封装到一个 `ItcastItem` 对象
            item = MyspyderItem()
            # extract()方法返回的都是unicode字符串
            name=each.xpath("./h3/text()").extract()
            title=each.xpath("./h4/text()").extract()
            info=each.xpath("./p/text()").extract()
            item["info"] = info[0]
            item["title"] = title[0]
            item["name"] = name[0]
            #items.append(item)

        #return items
            #传给管道文件
            yield item



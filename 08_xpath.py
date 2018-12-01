#coding=utf-8
import os
import urllib
import urllib2
from urllib2 import urlopen
from lxml import etree
class Spider():
    def __init__(self):
        self.teibaName= raw_input("需要爬取的贴吧:")
        self.beginPage=int(raw_input("请输入开始页码:"))
        self.endPage=int(raw_input("请输入结束的页码:"))

        self.url="https://tieba.baidu.com/f"
        self.headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        #图片的编号
        self.userName = 1


    def teibaSpider(self):
        for page in range(self.beginPage,self.endPage+1):
            pn=(page-1)*50
            word={"pn":pn,"kw":self.teibaName}
            word=urllib.urlencode(word)#改成url的编码模式
            myurl=self.url+'?'+word
            # 示例：http://tieba.baidu.com/f? kw=%E7%BE%8E%E5%A5%B3 & pn=50
            # 调用 页面处理函数 load_Page
            # 并且获取页面所有帖子链接,
            links = self.loadPage(myurl)
        print("下载完成,谢谢使用")
    #读取页面的内容
    def loadPage(self,url):
        request=urllib2.Request(url,headers=self.headers)
        response=urllib2.urlopen(request)
        html=response.read()
        #用xpath解析html
        selector=etree.HTML(html)
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for item in links:
            link = "http://tieba.baidu.com" + item
            #下载图片
            self.loadImage(link)
    def loadImage(self,link):
        req = urllib2.Request(link, headers=self.headers)
        html = urllib2.urlopen(req).read()

        selector = etree.HTML(html)

        # 获取这个帖子里所有图片的src路径
        imagesLinks = selector.xpath('//img[@class="BDE_Image"]/@src')
        for image in imagesLinks:
            self.writeImage(image)
    def writeImage(self,imageLink):
        print(imageLink)
        print("正在存储文件 %d"%self.userName)

        file = open('images/' + str(self.userName)  + '.jpg', 'wb')
        images = urllib2.urlopen(imageLink).read()
        file.write(images)
        file.close()
        self.userName += 1
        # filename=imageLink[-10:]
        # with open(filename,"wb") as f:
        #     f.write(images)

if __name__ == "__main__":

    # 首先创建爬虫对象
    mySpider = Spider()
    # 调用爬虫对象的方法，开始工作
    mySpider.teibaSpider()







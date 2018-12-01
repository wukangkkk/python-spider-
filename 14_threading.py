#coding=utf-8
import requests
from Queue import Queue
from lxml import etree
import threading
import time
import json

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        #调用父类初始化方法
        #threading.Thread.__init__(self),这是重点内容好好取理解
        super(ThreadCrawl, self).__init__()
        self.threadName=threadName
        self.pageQueue=pageQueue
        self.dataQueue=dataQueue
        self.headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        print ("启动"+self.threadName)
        while not CRAWL_EXIT:
            try:
                #取出一个数字,先进先出
                #可选参数block ,默认值为True
                #如果队列为空的话,block为True,不会结束,会进入阻塞阶段,直达队列有新数据
                #如果队列空的话,block为False,就会出现一个Quenue.empty()异常
                page=self.pageQueue.get(False)
                url="https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                content=requests.get(url,headers=self.headers)
                self.dataQueue.put(content)
            except:
                pass

        print ("结束"+self.threadName)
class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,filename):
        super(ThreadParse,self).__init__()
        self.threadName=threadName
        self.dataQueue=dataQueue

        self.filename=filename
    def run(self):
        print("启动"+self.threadName)
        while not PARSE_EXIT:
            try:
                html=self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
        print("结束"+self.threadName)
    def parse(self,html):
        result = html.xpath('//div[contains(@id,"qiushi_tag_")]')
        for site in result:
            # 取标签里面的东西用text
            # 用户的信息
            item = {}
            username = site.xpath('.//h2')[0].text
            # 段子的内容
            content = site.xpath('.//div[@class="content"]/span')[0].text
            # 投票次数
            vote = site.xpath('.//i')[0].text
            # 评论信息数量
            comments_numbers = site.xpath('.//i')[1].text
            # 保存信息在json文件中
            item['username'] = username
            # item['detailLink'] = url + detailLink
            item['content'] = content
            item['vote'] = vote
            item['comments_numbers'] = comments_numbers
            # 禁用ascii编码，按utf-8编码
            line = json.dumps(item, ensure_ascii=False)
            self.filename.write(line.encode('utf-8') + '\n')
            self.filename.close()





CRAWL_EXIT=False
PARSE_EXIT=False
def main():
    filename=open("duanzhi.json",'a')
    #初始化网页1-10个页面
    pageQueue=Queue(10)
    #采集结果的数据队列,参数为空表示不限制
    dataQueue=Queue()
    for page in range(1,11):
        pageQueue.put(page)
    #存储线程
    crawlthreads=[]
    #采集线程
    crawlList=["采集线程1号","采集线程2号","采集线程3号"]
    for threadName in crawlList:
        thread=ThreadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        crawlthreads.append(thread)
    #解析线程
    parseList=["解析线程1号","解析线程3号","解析线程3号"]
    threadparse=[]
    for threadName in parseList:
        thread=ThreadParse(threadName,dataQueue,filename)
        thread.start()
        threadparse.append(thread)
    #等待pageQueue为空,也就是等待之前的操作完毕
    while not pageQueue.empty():
        pass
    #如果采集队列为空,退出队列循环
    global CRAWL_EXIT

    CRAWL_EXIT=True
    print("pageQueue为空")
    #加阻塞,防止采集线程没结束,主线程就结束
    for thread in crawlthreads:
        thread.join()

if __name__=="__main__":
    main()
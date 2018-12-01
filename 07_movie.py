#coding=utf-8

import urllib2
import re
from lxml import etree


class Spyder():
    # initial the program
    def __init__(self):
        self.page = 1
        self.switch = True

    def loadPage(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }

        url = "https://www.80s.tw/movie/list/----g-p/" + str(self.page)
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        self.dealPage(html)


    def dealPage(self, html):
        pattern = re.compile('<h3\sclass="h3">(.*?)</h3>', re.S)
        content_list = pattern.findall(html)
        self.writePage(content_list)


    def writePage(self, content):
        for item in content:
            print item.decode("utf-8")
            with open("duanzhi.txt", "a") as f:
                f.write(item)


    def startWork(self):
        while self.switch:
            self.loadPage()
            command = input("如果继续爬取请按回车,退出请按(quit):")
            if command == "quit":
                self.switch = False
            self.page += 1


if __name__ == '__main__':
    movieSpyder = Spyder()

    movieSpyder.startWork()

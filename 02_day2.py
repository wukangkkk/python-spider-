#coding=utf-8
import urllib
import urllib2
from lxml import etree

def writeImage(imageLink,i):
    print(imageLink)
    print("正在存储文件 " )
    file = open('images/' + str(i)+'.jpg', 'wb')
    images = urllib2.urlopen('https:'+imageLink).read()
    file.write(images)
    file.close()
headers={
	 "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
     }

url="https://search.jd.com/Search?keyword=%E6%B5%B7%E9%B2%9C&enc=utf-8&spm=2.1.0"


request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
html=response.read()

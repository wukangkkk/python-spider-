#coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import urllib2
import time
url="https://search.jd.com/Search?keyword=%E6%B5%B7%E9%B2%9C&enc=utf-8&spm=2.1.0"
driver=webdriver.Chrome()
driver.get(url)
for i in range(1,10):
    js = "var q=document.documentElement.scrollTop=20000"
    driver.execute_script(js)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(9)

html=driver.page_source

count=0
selector=etree.HTML(html)
for item in selector.xpath('//li[@class="gl-item"]'):
    title=item.xpath('.//div[@class="p-name p-name-type-2"]//em/text()')[0]
    if len(title.split())>2:
        gtitle=title.split()[1][0:7]
        gprice = item.xpath('.//div[@class="p-price"]//i/text()')[0]
        pic = item.xpath('.//div[@class="p-img"]/a/img/@src')[0]
        gpic = 'https:' + pic
        count+=1
        str1='insert into df_goods_goodsinfo(gtitle,gpic,gprice,isDelete,gunit,gclick ,gjianjie,gkucun ,gcontent ,gtpye_id)\
         values('+gtitle+',df_goods/'+str(count) +',44,False,"500g" ,666,"好好好",88,"美味",1)'
        with open("data.txt", "a") as f:
            f.write(str1 + '\n')
            f.close
        #writeImage(gpic,count)
        # print(count)
        # print(gprice)
        # print(gpic)
        # print(gtitle.encode('utf-8'))
# insert into df_goods_goodsinfo(gtitle,gpic,gprice,isDelete,gunit,gclick ,gjianjie,gkucun ,gcontent ,gtpye_id)
# values('黄大鱼','df_goods/fish1',44,False,'500g' ,666,'好好好',88,'美味',1)
def writeImage(imageLink,count):
    print(imageLink)
    print("正在存储文件 %d"%count)
    file = open('images/' +str(count) + '.jpg', 'wb')
    images = urllib2.urlopen(imageLink).read()
    file.write(images)
    file.close()
with open("data.txt","w") as f:
    for i in a:
        test2 = i.encode('UTF-8')
        f.write(test2)
    f.close

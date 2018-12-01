#coding=utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver=webdriver.Chrome()
driver.get('https://www.douyu.com/directory/all')
while True:
    soup=BeautifulSoup(driver.page_source.encode('utf-8'),'lxml')
    titles=soup.find_all('h3',{'class':'ellipsis'})
    number=soup.find_all('span',{'class':'dy-num fr'})
    for title,num in zip(titles,number):
        print (u"观众人数:" + num.get_text().strip(), u"\t房间标题: " + title.get_text().strip())

    if driver.page_source.find('shark-pager-disable-next') != -1:
        break
        # 模拟下一页点击
    driver.find_element_by_class_name('shark-pager-next').click()



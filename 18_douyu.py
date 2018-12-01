#coding=utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup

class douyuSelenium(unittest.TestCase):
    def setUp(self):
        #初始化方法
        self.driver=webdriver.PhantomJS()

    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            soup=BeautifulSoup(self.driver.page_source,'lxml')
            #斗鱼直播标题
            titles=soup.find_all("h3",{"class":"ellipsis"})
            nums=soup.find_all("span",{"class":"dy-num fr"})
            for title,num in zip(titles,nums):
                print(u"观众人数:"+num.get_text().strip())

            if self.driver.page_source.find("shark-pager-disable-next")!=-1:
                break
            #模拟点击下一页
            self.driver.find_element_by_class_name('shark-pager-next').click()

    def tearDown(self):
        print("加载完成...")
        self.driver.quit()


if __name__=="___main___":
    unittest.main()




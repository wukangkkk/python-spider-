#coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
time.sleep(3)
driver.get('http://www.baidu.com/')

data=driver.find_element_by_id("wrapper").text
print(data)


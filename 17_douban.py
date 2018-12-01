#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.douban.com/")
#输入帐号和密码
driver.find_element_by_id("form_email").send_keys("517841670@qq.com")
driver.find_element_by_id("form_password").send_keys("wukang199427")

#点击进入网页
driver.find_element_by_class_name("bn-submit").click()
time.sleep(3)
driver.save_screenshot("douban.png")
print driver.page_source
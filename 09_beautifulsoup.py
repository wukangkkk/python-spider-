#coding=utf-8
from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p> """
#创建beautiful soup 对像.
soup=BeautifulSoup(html,"lxml")
#find_all 收索文档树
#print (soup.find_all('a'))
# for tag in soup.find_all(re.compile("^a")):
#     print (tag)
#print(soup.find_all(id="link1"))

#print soup.select('a')

print soup.select('p #link1')

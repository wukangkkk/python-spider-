#coding=utf-8
import requests
from lxml import etree
import json

url="https://www.qiushibaike.com/8hr/page/1/"
headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
response=requests.get(url,headers=headers)
#在request请求中,返回的值要用text
reshtml=response.text
html=etree.HTML(reshtml)
result=html.xpath('//div[contains(@id,"qiushi_tag_")]')
output=open('chuishi.json','w')
for site in result:
    #取标签里面的东西用text
    #用户的信息
    item={}
    username= site.xpath('.//h2')[0].text
    #段子的内容
    content=site.xpath('.//div[@class="content"]/span')[0].text
    # 投票次数
    vote = site.xpath('.//i')[0].text
    # 评论信息数量
    comments_numbers= site.xpath('.//i')[1].text
    #保存信息在json文件中
    item['username'] =username
    #item['detailLink'] = url + detailLink
    item['content'] =content
    item['vote'] = vote
    item['comments_numbers'] =comments_numbers
    # 禁用ascii编码，按utf-8编码

    line = json.dumps(item, ensure_ascii=False)
    output.write(line.encode('utf-8')+'\n')
output.close()


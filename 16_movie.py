#coding=utf-8
import requests
import re
from lxml import etree
import json
import pandas as pd
import csv
import matplotlib.pyplot as plt
def get_one_page(url):
    headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        return None
    #利用正则表达式求特定的目标
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(d+)</i>', re.S)
    # re.S表示匹配任意字符，如果不加，则无法匹配换行符
    items = re.findall(pattern, html)
    print(items)
    #利用xpath求需要的内容
def get_realease_area(data):
    #data='2018-10-10 (美国)'
    pattern=re.compile(r'.*((.*))')
    items=re.search(pattern,data)
    if items is None:
        return '未知'
    return items.group(1)
def parse_one_page_xpath(html):
    parse=etree.HTML(html)
    items=parse.xpath('//*[@id="app"]//div//dd')
    for item in items:
        yield {
            'index':item.xpath('./i/text()')[0],
            'name':item.xpath('.//p/a/@title')[0],
            'releasetime':item.xpath('.//p[@class="releasetime"]/text()')[0].strip()[5:],
            'star':item.xpath('.//p[@class="star"]/text()')[0].strip()[3:],
            'score':item.xpath('.//p/i[@class="integer"]/text()')[0]+item.xpath('.//p/i[@class="fraction"]/text()')[0]
        }

    #自己的代码方法
    # for item in items:
    #     dict={}
    #     index=item.xpath('./i/text()')[0]
    #     name=item.xpath('.//p/a/@title')[0]
    #     star=item.xpath('.//p[@class="star"]/text()')[0].strip()[3:] #用于除掉字符串中的空格
    #     releasetime=item.xpath('.//p[@class="releasetime"]/text()')[0].strip()[5:]
    #     sorce=item.xpath('.//p/i[@class="integer"]/text()')[0]+item.xpath('.//p/i[@class="fraction"]/text()')[0]
    #     dict['index']=index
    #     dict['name']=name
    #     dict['start']=star
    #     dict['releasetime']=releasetime
    #     dict['sorce']=sorce
    #     line = json.dumps(dict, ensure_ascii=False)
    #     output.write(line.encode('utf-8')+'\n')
    # output.close()
def write_to_files(con_list):
    #with open('猫眼top100.csv', 'a', encoding='utf_8_sig', newline='') as f:
        # 'a'为追加模式（添加）
        # utf_8_sig格式导出csv不乱码
        # fieldnames = ['index',  'name', 'star', 'releasetime',  'score']
        # w = csv.DictWriter(f, fieldnames=fieldnames)
        # w.writerow(item)
    df = pd.DataFrame(con_list, columns=['index', 'name', 'star', 'releasetime', 'score'])
    df.to_csv('猫眼top100.csv', index=False, encoding='utf_8_sig')

def plot_top10():
    plt.style.use('ggplot')
    fig=plt.figure(figsize=(8,5))
    color1='#6D6D6D'



def main():
    # con_list=[]
    # for i in range(10):
    #     url="http://maoyan.com/board/4?offset="+str(i*10)
    #     #提取一个网页的源代码
    #
    #     html=get_one_page(url)
    #     for item in parse_one_page_xpath(html):
    #         con_list.append(item)
    # write_to_files(con_list)
    pass



if __name__=="__main__":
    main()
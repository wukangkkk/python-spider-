#coding=utf-8
import urllib2
import jsonpath
import json
import chardet
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
request=urllib2.Request(url)
response=urllib2.urlopen(request)
html=response.read()
#把json格式的字符串转化为python字符串
jsonobj=json.loads(html)
city_list=jsonpath.jsonpath(jsonobj,'$..name')
for item in city_list:
    print item

fp = open('city.json','w')

content = json.dumps(city_list, ensure_ascii=False)
print content

fp.write(content.encode('utf-8'))
fp.close()
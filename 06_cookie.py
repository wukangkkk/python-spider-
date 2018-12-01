#coding=utf-8
import urllib2
import cookielib

#构建一个CookieJar对象实例保存cookie
cookiejar=cookielib.CookieJar()
#使用HTTPCookieProcessor()创建cookie处理器,参数为CookieJar()对象
handler=urllib2.HTTPCookieProcessor(cookiejar)
#通过build_opener来构建opener
opener=urllib2.build_opener(handler)

#4 以get 方法访问页面,访问后会自动保存在cookiejar中
opener.open("http://www.baidu.com")
cookieStr=""
for item in cookiejar:
	cookieStr=cookieStr+item.name+"="+item.value+";"

print cookieStr[: -1]
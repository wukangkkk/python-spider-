#coding=utf-8
# import urllib2
# #构建2个代理handler,一个有代理ip,一个没有代理ip
# httpproxy_handler=urllib2.ProxyHandler({"http":"123.88.67.81:80"})
# nullproxy_handler=urllib2.ProxyHandler({})
# #定义一个开关
# proxy_switch=False
# if  proxy_switch:
# 	opener=urllib2.build_opener(httpproxy_handler)
# else:
# 	opener=urllib2.build_opener(nullproxy_handler)
# request=urllib2.Request("http://www.baidu.com/")
# response=opener.open(request)
# print response.read()
import urllib2
import urllib
#私密代理授权的账户
user="wukang"
passwd="wukangwukang"
#私密代理的ip
proxyserver="192.168.128.1:8080"
#1 构建一个密码管理对象,用来保存要处理的用户名和密码

passwdmgr=urllib2.HTTPPasswordMgrWithDefaultRealm()
#2 添加账户信息,第一个参数是realm是与远程服务器相关的域的信息,一般没人管他都是写None
passwdmgr.add_password(None,proxyserver,user,passwd)
#3 构建一个代理基础用户名/密码验证ProxyBasicAUthHandler处理器对象,参数是创建的密码管理对象
proxyauth_handler=urllib2.ProxyBasicAuthHandler(passwdmgr)
#4 通过build_opener()方法用这些代理Handler()对象,创建自定义的opener对象
opener=urllib2.build_opener(proxyauth_handler
request=urllib2.Request("http://www.baidu.com/")

response=opener.open(request) 

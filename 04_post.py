#coding=utf-8
import urllib
import urllib2


#url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
formdata={
	"i":"hello",
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"1539738658231",
	"sign":"f3de4976afd705ddcca68b5e59f6a502",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_REALTIME",
	"typoResult":"false"

}


data=urllib.urlencode(formdata)

request=urllib2.Request(url,data=data,headers=headers)

response=urllib2.urlopen(request)

print(response.read())
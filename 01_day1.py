
import urllib2


headers={
	 "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
     }
request=urllib2.Request("https://www.80s.tw/movie/list/----g-p/3",headers=headers)
response=urllib2.urlopen(request)
#html=response.read()


print response.getcode()

print response.info()
#coding=utf-8
from bs4 import BeautifulSoup
import  requests
def zhihuLogin():
    #构建一个session对象,可以保存cookies
    sess=requests.Session()
    headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    #首先获取登录页面信息,找到需要的POST信息(_xsrf),同时记录网页的cookies值
    html=sess.get("https://www.zhihu.com/signup?next=%2F",headers=headers).text#也可以content
    bs=BeautifulSoup(html,"lxml")
    #_xsrf 防止CSRF攻击(跨栈请求伪造)
    _xsrf=bs.find("input",attrs={"name":"_xsrf"})



if __name__=="__main__":
    zhihuLogin()
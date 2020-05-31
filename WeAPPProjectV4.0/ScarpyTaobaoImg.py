# -*- coding: utf-8 -*-

#从淘宝链接中获取图片链接，并返回
import requests
from bs4 import BeautifulSoup 
import os#没用到
#import codecs#没用到
#import selenium#没用到
#import csv #必须加入csv模块，否则之后csv write有问题
import re
import time


#定义解析函数，获取initial购物链接，网络地址
def getUrl(str):
    pattern = re.compile('[a-zA-z]+://[^\s]*')
    url = pattern.findall(str)
    print url[0]
    return url[0]
#定义请求函数，获取response即html数据
def getHTML(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    r=requests.get(url,headers=headers)
    #print r.content
    #print r.content
    return r.content
#定义解析函数，获取淘宝链接的长链接地址
def getLongHref(html):
    soup = BeautifulSoup(html,'html.parser')
    ele_script = soup.find_all('script')
   # ele_script是一个 bs4.tag,用contents获取标签的内容
    text_include_longHref = ele_script[1].contents
    #标签的内容是一个list

    #把list转换为字符串
    string = text_include_longHref[0]
    #将字符串以；分号分开,*****0000000*正则表达式优化
    list = re.split(';',string)
    #然后用单引号分号分割开，获取目标地址
    href = re.split('\'',list[2])[1]
    #print href
    return href
#定义解析函数，获取淘宝图片的链接
def getIMG_Href(html):
    img_href_list = []
    soup = BeautifulSoup(html,'html.parser')
    #用soup查找带有data-value属性的标签
    tag_include_img= soup.find_all('li',attrs={'data-value':True,'title':True})
    #print tag_include_img, 可以用迭代器提高效率**0000**
    for tag in tag_include_img:
        #将unicode转换为字符串
        str= tag.find('a')['style'].encode("utf-8")
        #print type(str)
        #用（ 左边括号分割*000000*，正则表达式可以优化
        str1 = re.split('\(',str)[1]
        #用 ）右括号分割,注意括号的转译
        str2 = re.split('\)',str1)[0]
        #用—_40分割,注意这有可能变哦，这块有的可能无大图，但是不影响链接
        str3 = re.split('\_40',str2)[0]
        #将爬来的网址加上http：//
        str3 = 'http:'+str3
        print str3
        #print "<li><span>%30s</span></li>"%str3
        #获取图片的链接租场的表
        img_href_list.append(str3)    
    return img_href_list

#--------------------------#
#main programme
#--------------------------#
if __name__ == "__main__":
	t1 = time.time()
	str = '【这个#聚划算团购#宝贝不错:男装 运动长裤 404166 优衣库UNIQLO(分享自@手机淘宝android客户端)】http://m.tb.cn/h.3aSYozt 点击链接，再选择浏览器打开；或复制这条信息€mFEu0EGGXBO€后打开淘宝'
	url = getUrl(str)
	#获取初始界面的内容
	html = getHTML(url)
	#获取长地址链接
	long_href= getLongHref(html)
	#获取购物页面response
	html1 = getHTML(long_href)
	#print html1
	#获取图像界面的链接
	getIMG_Href(html1)
	t2 = time.time()
	print t2-t1

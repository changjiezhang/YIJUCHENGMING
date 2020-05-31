# -*- coding: utf-8 -*-

from flask import Flask,request,url_for,render_template

from  ScarpyTaobaoImg import getUrl,getHTML,getLongHref,getIMG_Href
from ImgTranspProces import  getUrlImage,transPNG
from ImgSaveCos import ImgUpload
import time
from ImgPath import imgPath
from ImgUrlMysql import insertDb,queryDb
import MySQLdb
#create the application object

app = Flask(__name__)
#定义一个全局变量
db = MySQLdb.connect('localhost','root','tsinghua858790','imgurl')
#这个路由用来欢迎界面
@app.route('/',methods=['get'])
def index():
	return render_template('index.html')
#这个路由用来获取淘宝图像的链接
@app.route('/getTaobaoImg',methods=['POST'])
def getTaobaoImg():
	#淘宝宝贝的地址,特别注意€符号，是无法print的因为是GBK的解析，解析不出来的
	#这块可以在地址端就解决掉短地址问题
	item_addr= request.form['item_addr']
	#使用替换，把€符号替换掉，使用本地手机*00000000**运算解决掉短地址问题提高效率
	#print item_addr
	#可获得字符里边的地址，其实可以省略掉
	url = getUrl(item_addr)
	#获取初始界面的内容
	html = getHTML(url)
	#获取长地址链接
	long_href= getLongHref(html)
	#获取购物页面response
	html1 = getHTML(long_href)
	#获取图像界面的链接
	imgurl_list= getIMG_Href(html1)
	#flask只能返回string，tuple格式数据
	imgurl_list_str = str(imgurl_list)
	#返回图片的网址进行手机端展示
	return imgurl_list_str
	
 #这个路由用来对选取的图像进行处理，并返回透明图片  
@app.route('/getProcessdImg',methods=['post'])
def getProcessdImg():
	global db;
	#获取网络图片地址,注意这块要优化，进行一个判断‘
	#如果是同一个url则必须跳转到以前的资源，否则造成浪费
	img_url = request.form['img_url']
	#访问数据库
	img_data = queryDb(db,img_url)
	print img_data
	if img_data:
		return img_data
	else:
		print('数据库中没，需要重新保存')
		#获取网络图片地址
		image = getUrlImage(img_url)
		#创建本地图片的路径
		img_path = imgPath()[0]
		img_name = imgPath()[1]
		#图像处理
		img = transPNG(image)
		#把图片上传到cos上
		ImgUpload(img,img_name) 
		#返回cos上的图片地址
		procesed_img_url = 'https://armirrorpro-1256515134.cos.ap-shanghai.myqcloud.com/'+img_name
		insertDb(db,img_url,procesed_img_url)
		return procesed_img_url
if __name__ == "__main__":
    #先链接数据库
	
	app.run()
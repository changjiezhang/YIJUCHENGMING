# -*- coding: utf-8 -*-
#python图像处理模块
#包含功能：
#1、实现白色背景，透明化
#2、实现将曲线检测，将头部领子区域的图像扣掉（暂时没实现）
from PIL import Image
#
#从网络地址获得图片
import requests
from io import BytesIO
#使用numpy对图像进行转置，不知道可行不
#import numpy as np


#定义函数，从网络获取图片，暂时没有实现哎
def getUrlImage(url):
    response = requests.get(url)
	#BytesIO打开的就是二进制流
    image = Image.open(BytesIO(response.content))
    #image.show()
	#返回一个image图像的数据流
    return image
#定义裁剪函数，去除图像中除了衣服外所有的透明边
def imgCrop(img):
	#print img
	datas = img.getdata()
	size_img = img.size
	#行数、列数
	row = size_img[0]
	coloumn = size_img[1]
	#print row
	#print coloumn
	#建立一个list
	datas = list(datas)
	#获取数组的长度
	#len_img = len(datas)
	#print len_img
	for items in datas:
		if items[3] > 0:
			index_0 = datas.index(items)
			#print index_0
			break;	
	column_0 = index_0/coloumn
	print column_0
	new_img = img.crop((0,column_0,row,coloumn))
	return new_img
#定义图像旋转函数
'''
def imgRotate(img):
	img_arr = np.array(img)
	print size(img_arr)
	img_arr = img_arr.T
	new_img = Image.fromarray(img_arr)
	return new_img
'''
#定义函数，将图片处理为背景透明
#修改说明，不必添加存储图像了，仅作为处理透明
#def transPNG(srcImg,destImg):
def transPNG(srcImg):
	#图像格式转换，增加透明通道
    img = srcImg.convert('RGBA')
    #img.show()
    datas = img.getdata()
    #print datas
    newData = list()
	#这块可以使用迭代器
    for item in datas:
        #print item
        #这条语句是，将偏白的像素点的A通道设计为0，就是将白色背景变成0
        #下边的这几个值是根据白色背景调试出来的
        #像素的平均值效果不是很好
        #aver_item =( item[0]+item[1]+item[2])/3
        if item[0] >238 and item [1] >238 and item[2] >241:
        #if aver_item >243:
            newData.append((255,255,255,0))
        else :
            newData.append(item)
    img.putdata(newData)
    #img.show()，这就是个二进制流，可以不用图片，可以直接返回给浏览器
	#可以借鉴，怎么把知乎图片的二进制流反馈给服务器
	#这可以图像存到腾讯的存储桶里边,每张图片0.5M图片量太大了，可以考虑删除
	#目前的最简单的版本就是，把图像缩小
    #img.save(destImg,'PNG')
    #img.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_1.png','PNG')
    #return img
	#第一次裁剪不需要旋转
    img = imgCrop(img)
	#进行4次旋转和裁剪次旋转和裁剪
    for i in range(0,3):
		img= img.transpose(Image.ROTATE_90)
		img=imgCrop(img)
    img = img.transpose(Image.ROTATE_90)
    return img
#main chengxu
#其实要注意一下这个URl，注意将从淘宝扒拉的是不带http的
#需要在爬来的网址前边加上http：//
if __name__ == "__main__":
	url = 'http://img.alicdn.com/imgextra/i2/196993935/TB29a3YbRfM8KJjSZFrXXXSdXXa-196993935.jpg'
	img = getUrlImage(url)
	newimg = transPNG(img)
	newimg.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_1.png','PNG')
	print newimg
	#new_img = newimg.crop((0,72,1000-72,1000))
	'''
	new_img =imgCrop(newimg)
	new_img.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_2.png','PNG')
	print new_img
	#单纯是用旋转是不对的，只是旋转了内容，图像的大小不变，即行列数不变
	new_img_1 = new_img.transpose(Image.ROTATE_90)
	new_img_1 =imgCrop(new_img_1)
	print new_img_1
	new_img_1.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_3.png','PNG')
	new_img_2 = new_img_1.transpose(Image.ROTATE_90)
	
	new_img_2 =imgCrop(new_img_2)
	print new_img_2
	new_img_2.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_4.png','PNG')
	new_img_3= new_img_2.transpose(Image.ROTATE_90)
	
	new_img_3 =imgCrop(new_img_3)
	print new_img_3
	new_img_3.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_5.png','PNG')
	new_img_4= new_img_3.transpose(Image.ROTATE_90)
	new_img_4.save('D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/T_blue_6.png','PNG')
	
	#transPNG(img)
	'''
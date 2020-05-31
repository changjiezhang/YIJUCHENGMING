# -*- coding: utf-8 -*-
#本程序的功能是
#实现图片到腾讯云cos的传递

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
from PIL import Image #进行image格式的存储
from io import BytesIO

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#bucket的初始配置
secret_id ='AKIDsEh071VHctzw1vjnqjS6f3Fdswo8ni8O'  #用户的secretId
secret_key ='BAxZ3MfqpcFgO1cgvHS8g3EF5kvztoaD'   #secret_key
region = 'ap-shanghai' #用户区域
token =''
config = CosConfig(Secret_id = secret_id, Secret_key = secret_key, Region = region,Token =token)
#获取客户端对象
client = CosS3Client(config)

#定义一个函数进行image的上传，直接接PIL的image对象
#将image对象直接存储到cos上
def ImgUpload(img,img_name):

	#roiImg = img.crop(box) #crop是提取某个矩形大小图像
	imgByteArr = BytesIO() #创建一个字节流
	img.save(imgByteArr,format='PNG') #把图像数据存到字节流里
	imgByteArr = imgByteArr.getvalue()
	
	response = client.put_object(
		Bucket = 'armirrorpro-1256515134',
		Body = imgByteArr,
		Key = img_name,
		StorageClass = 'STANDARD',
		ContentType ='image/jpeg',
	)
	print (response['ETag'])
	

#单独脚本的尝试
img_path = 'D:/Chuangye_AP/WcechatLiteAPP/pythonPrograme/WeAPPProject/clothtype5.png' #这会自动在存储里边建立相同的文件夹
img_name = 'testImg.png'
if __name__ == "__main__":
	img = Image.open(img_path)
	ImgUpload(img,img_name)
	
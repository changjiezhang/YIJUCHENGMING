# -*- coding: utf-8 -*-
#生成图片文件的名称
import time
import os
import sys

#定义个函数生成图片的路径
def imgPath():
    now_time = time.time()
    time_str = str(now_time)
	#获取时间字符串，以ms计算的
    time_str = time_str.replace('.','')
    #获取当前脚本的路径，在当前文件路径下创建
    img_name = time_str+'.png'
    img_path = sys.path[0].replace('\\','/')+'/static/'+img_name
    return img_path,img_name

if __name__ == "__main__":
    imgpath= imgPath()
    print imgpath
    print sys.path[0].replace('\\','/')


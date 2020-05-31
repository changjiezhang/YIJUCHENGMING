#!/usr/bin/python
# -*- coding: UTF-8 -*-

#这个函数的目的是
#1、将淘宝图像的原始链接和处理后的链接存在数据库里
#2、进行判断，如果数据库里边有，则返回数据库信息
#如果没有，就是对图像进行处理
#输入：淘宝图像地址，输出：腾讯云处理后的图像地址

import MySQLdb

#在表中插入数据
def insertDb(db,img_url,processed_img_url):
	#使用cursor方法
	cursor = db.cursor()
	#SQL插入语句
	sql = "INSERT INTO imgurls(taobaoimgurl,processedurl)\
		   values('%s','%s')" %(img_url,processed_img_url)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print '插入数据失败'
		db.rollback()

#查询数据库
#如果已经有了，就返回查询结果
#如果没有，就进行处理然后，写数据库，存cos
#这个函数返回的是处理后的peocessed_imgurl
def queryDb(db,img_url):
	#使用cursor方法获取操作游标
	cursor = db.cursor()
	#Sql查询语句
	sql = "SELECT * FROM imgurls \
		WHERE taobaoimgurl= '%s'" % img_url
	#注意加上单引号
	print sql
	try:
		#执行SQL语句
		cursor.execute(sql)
		#获取记录列表
		results = cursor.fetchall()
		#获取唯一的记录，和已经处理过的img_url
		processed_img_url = results[0][1]
		print processed_img_url
		return processed_img_url
	except:
		print "Error:unable to fetch data"
		#怎么把processed_img_url 传进来
		#是不是可以传递一个状态量，有或者无
		return False
		


if __name__ == "__main__":
    db = MySQLdb.connect('localhost','root','123456','imgurl')
    print('连上了')
    img_url ='258'
    data = queryDb(db,img_url)
    print data
    if data:
        print data
    else:
	    print('插入数据')
	    insertDb(db,img_url,'456')



	

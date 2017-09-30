#-*- coding: UTF-8 -*-
#coding=utf-8

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("172.21.12.120","tmp","tmp","userservicetest" )
#db = MySQLdb.connect("172.21.12.98","tmp","tmp","zabbix34" )
db.set_character_set('utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# cursor.execute('SET NAMES utf8;')
# cursor.execute('SET CHARACTER SET utf8;')
# cursor.execute('SET character_set_connection=utf8;')

# 使用execute方法执行SQL语句
cursor.execute("select * from appinfo limit 11")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
testdata = (1, '你好', 22)
print data
print testdata , testdata[1]
#print "Database version : %s " % data[0]

# 关闭数据库连接
db.close()
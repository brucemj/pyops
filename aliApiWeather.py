# -*- coding: UTF-8 -*-
import urllib, urllib2, sys
import pprint

# https://apigateway.console.aliyun.com/inner/?spm=5176.730006-cmapi014302.102.10.c4Xjqb#/cn-beijing/apps/testApi/db6880d725244399b8128c1c3846cfe2/0992e2b3fa5e4f1c91215b933a6f8901/RELEASE/24622672/CloudMarket
host = 'http://jisutqybmf.market.alicloudapi.com'
path = '/weather/query'
method = 'GET'
appcode = '69ba19057218493f962a441672766cda'
querys = 'city=%E5%AE%89%E9%A1%BA&citycode=citycode&cityid=cityid&ip=ip&location=location'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
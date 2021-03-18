'''
爬取豆瓣电影数据
了解ajax 爬取方式
'''

from urllib import request, parse

import json


url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100"
# get方式发送  参数形式进行发送
# post方式发送， form形式   加密的（有道词典？）


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# 经过测试发现如果不加UA 会报错httperror 418

req = request.Request(url=url, headers=headers)

rsp = request.urlopen(req)

data = rsp.read().decode()
print(type(data))

data = json.loads(data)

print(type(data))
#print(data)

for i in data:
    # print(i)
    # print(type(i))
    print(i["rating"], i["rank"], i["title"])







'''
利用parse模块模拟post请求
分析百度词典
分析步骤
1 打开F12
2 尝试输入单词girl  发现每敲一个字母后都有请求
3 请求地址是  https://fanyi.baidu.com/sug
4 利用NwtWork-All-Headers  查看 发现FormData的值是 kw:girl
5 检查返回内容格式，发现返回的是json格式内容-----需要用到json包
'''

import requests

from urllib import parse
# 负责处理json格式的模块
import json

'''
大致流程是：
1 利用data构造内容  然后用urlopen打开
2 返回一个json格式的结果
3 结果就一个个是girl的释义
'''

baseurl = "https://fanyi.baidu.com/sug"

# 存放用来模拟form的数据一定是dict格式
data = {
    # girl 是需要翻译的英文内容  应该是由用户输入，此时使用硬编码
    'kw': 'girl'
}

# 需要用parse模块对data进行编码
# 需要用encode编码成字节流  这是urllib要求的

# 下面不能使用bytes类型， 直接使用dict类型就可以
# data = parse.urlencode(data).encode()
# print(type(data))

# 我们需要构造一个请求头，请求头应该至少包含传入的数据长度
# request 要求传入的请求头是一个dict格式 *** 一定是dict ***

headers = {
    # 因为使用post  至少应该包含content-length字段
    'Content-Length':str(len(data))
}


# rsp = request.urlopen(baseurl,data = data, headers= headers)


rsp = requests.post(baseurl, data=data, headers= headers)
# rsp = request.urlopen(baseurl,data = data)

print(rsp.text)
print(rsp.json())


# for item in json_data['data']:
#     # print(type(item))
#     # print(item)
#     print(item['k'], '----', item['v'])


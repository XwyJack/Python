'''
任务要求跟v5一样
本案例只是利用Request来实现v5的内容

利用parse模块模拟post请求
分析百度词典
分析步骤
1 打开F12
2 尝试输入单词girl  发现每敲一个字母后都有请求
3 请求地址是  https://fanyi.baidu.com/sug
4 利用NwtWork-All-Headers  查看 发现FormData的值是 kw:girl
5 检查返回内容格式，发现返回的是json格式内容-----需要用到json包
'''

from urllib import request, parse

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
# 需要用encode编码成字节流
data = parse.urlencode(data).encode()
print(type(data))

# 我们需要构造一个请求头，请求头应该至少包含传入的数据长度
# request 要求传入的请求头是一个dict格式 *** 一定是dict ***

headers = {
    # 因为使用post  至少应该包含content-length字段
    'Content-Length': len(data)
}

# 构造一个Request的实例

req = request.Request(baseurl, data=data, headers=headers)

# 因为已经构造了一个Request类的请求实例， 则所有的请求信息都可以封装在Request实例中
rsp = request.urlopen(req)

# 下面就不使用了
# rsp = request.urlopen(baseurl,data = data, headers= headers)
# rsp = request.urlopen(baseurl,data = data)


json_data = rsp.read().decode('utf-8')

print(json_data)


# 把json字符串转化为字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

print("-------------")
print(type(json_data['data']))
print(json_data['data'])
# josn_data 是字典  <class 'dict'>
# json_data['data'] 是列表  <class 'list'>  如下：
# [{'k': 'girl', 'v': 'n. 女孩; 姑娘，未婚女子; 女职员，女演员; （男人的）女朋友'}, {'k': 'GIRL', 'v': 'abbr. Generalised Information Retrieval Language <'}, {'k': 'girls', 'v': 'n. 女孩; 女儿( girl的名词复数 ); 女工; （男人的）女朋友'}, {'k': 'GIRLS', 'v': 'abbr. Generalized Information Retrieval and Listin'}, {'k': 'girly', 'v': 'adj. <非正>（杂志或图片）以表现裸体女子为特色的'}]
# json_data['data'] 中的每一个item又是字典, 如下：
# {'k': 'girl', 'v': 'n. 女孩; 姑娘，未婚女子; 女职员，女演员; （男人的）女朋友'}
# 然后再取每个item字典中的k值和v值

print("--------------")

for item in json_data['data']:
    # print(type(item))
    # print(item)
    print(item['k'], '----', item['v'])


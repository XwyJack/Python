import requests

url = "http://www.baidu.com"
# 两种请求方式
# 使用get请求
rsp = requests.get(url)
print(type(rsp))
print(rsp.text)

# 使用requset请求

rsp = requests.request("get",url)
print(rsp.text)


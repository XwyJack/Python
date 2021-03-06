'''
访问一个网址
更改自己的UA 进行伪装
'''

from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baidu.com"

    try:

        # 使用head方法进行伪装UA
        # headers = {}
        # headers['UserAgent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg"
        # req = request.Request(url, headers= headers)

        # 使用add_header 方法

        req = request.Request(url)
        req.add_header("UserAgent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg")

        # 正常访问
        rsp = request.urlopen(req)

        html = rsp.read().decode()

        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

    print("None")
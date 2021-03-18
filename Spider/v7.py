'''
URLError使用

'''

from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baiiiiiiiiiiidu.com"
    # 一定要把爬的代码用try括起来
    try:

        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError : {0}".format(e))
        print("URLError : {0}".format(e.reason))
    except Exception as e:
        print(e)
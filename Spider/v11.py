'''


'''

from urllib import request, error

if __name__ == '__main__':

    # url = "http://www.163.com/"
    url = "https://mail.qq.com/"
    # url = "http://www.baidu.com/"
    rsp = request.urlopen(url)

    # print(rsp.read().decode('unicode_escape'))
    # print(rsp.read().decode('gbk'))
    # 163竟然使用的是gbk编码
    html = rsp.read().decode('gbk')
    print(html)

    with open("qq.html","w") as f:
        f.write(html)

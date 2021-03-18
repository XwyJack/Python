from urllib import request, parse

if __name__ == '__main__':

    url = "http://www.baidu.com/s?"  #  后面的s？ 表明后面是参数
    wd = input("Inout your keyword: ")

    # 要想使用data  需要使用字典结构

    qs = {
        "wd": wd
    }

    # 转化url编码  使用parse进行编码的方法

    qs = parse.urlencode(qs)
    print(qs)

    # 如果直接用可读的带参数url  是不能访问的
    fulrul = url + qs

    print(fulrul)

    rsp = request.urlopen(fulrul)

    html = rsp.read()

    html = html.decode()

    print(html)


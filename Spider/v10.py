'''
使用代理访问百度网站

'''


from urllib import request, error


if __name__ == '__main__':

    url = "http://www.baidu.com"

    # 使用代理步骤
    # 1.设置代理地址
    proxy = {'http': '175.42.128.26:9999'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    # 现在如果访问url  则使用代理服务器

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()

        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)


# 上面的案例报错了  因为 <urlopen error [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。>
# 可能是代理连接不上
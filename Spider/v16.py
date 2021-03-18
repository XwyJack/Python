
from urllib import request, error, parse
from http import cookiejar


# 创建cookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 由于qq的页面没有找到相关的用户名密码登录的字段  所以没有完成此案例
# 现在换由人人网测试





def getHomepage():

    url = "http://www.renren.com/976410643/profile"

    # 如果已经执行了login函数，则opener 自己已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("renren3.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == '__main__':

    getHomepage()


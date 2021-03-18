
from urllib import request, error, parse
from http import cookiejar


# 创建cookiejar的实例
cookie = cookiejar.CookieJar()

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


def login():

    '''
    负责初次登录
    需要输入用户名密码
     用来获取cookie
    '''


    # url = "https://mail.qq.com/cgi-bin/frame_html?sid=KmgcbXK0Qaj6FSRE&r=01eff76236a38cc37ee55d4c07ddd341/"
    # 此url需要从form的action中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登录的form的两个对应input中提取name属性
    data = {
        "email": "18514587109",
        "password": "1qaz@WSX"
    }

    # 把数据进行编码

    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data= data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    '''
    执行完login之后 会得到授权之后的cookie
    尝试把cookie打印出来
    '''
    login()

    print(cookie)

    for item in cookie:
        print("-------------")
        print(type(item))
        print(item)

        for i in dir(item):
            print(i)



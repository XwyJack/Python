'''
破解有道词典
v1
'''

from urllib import request, parse


def youdao(key):

    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {

        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16160553737146",  # 加盐
        "sign": "f3b122ecd93638d554993044a55729eb",  # 签名
        "lts": "1616055373714",
        "bv": "a70166da0759fd61f4c3fd22f18d04e3",
        "doctype": "json",
        "version":"2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    # 参数data需要是bytes格式

    data = parse.urlencode(data).encode()


    headers = {
                "Accept": "application/json, text/javascript, */*; q= 0.01",
                # "Accept-Encoding": "gzip,deflate",
                "Accept-Language": "zh-CN,zh;q=0.9;en;q=0.8, en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "Content-Length": "238",
                "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8",
                "Cookie": "OUTFOX_SEARCH_USER_ID = -1213192585 @ 10.108.160.101;JSESSIONID = aaa3mCVmM1WduaM66zeHx;OUTFOX_SEARCH_USER_ID_NCOO = 2104214362.9143758;___rl__test__cookies = 1616055373712",
                "Host": "fanyi.youdao.com",
                "Origin": "http://fanyi.youdao.com",
                "Referer": "http://fanyi.youdao.com/",
                "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg / 89.0.774.54",
                "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data= data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)


if __name__ == '__main__':
    youdao("girl")
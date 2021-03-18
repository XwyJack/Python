'''
破解有道词典
v2
处理js加密代码

salt：
r = "" + (new Date).getTime(),
i = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);

sign：
n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")

上面可见：
md5一共需要四个参数，第一个和第四个都是固定的字符串，  第三个是所谓的盐， 第二个是。。。。
第二个参数就是需要输入的要查找的单词

'''

from urllib import request, parse


def getSalt():

    '''


    :return:
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0, 10)

    return salt


def getMD5(v):

    import hashlib

    md5 = hashlib.md5()

    # update需要bytes格式参数

    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign


def getSign(key):

    sign =  "fanyideskweb" + key + str(getSalt()) + "Tbh5E8=q6U3EXe+&L[4c@"
    sign = getMD5(sign)

    return sign


from urllib import request, parse


def youdao(key):

    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {

        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(getSalt()),  # 加盐
        "sign": getSign(key),  # 签名
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
                "Content-Length": len(data),
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
    youdao("sex")
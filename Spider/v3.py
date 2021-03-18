from urllib import request
import chardet

if __name__ == '__main__':
    # 直接爬不好用  就需要传入header

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Cookie": "__gads=ID=4d781462e1bae3db-221c059762c6003b:T=1615685911:RT=1615685911:S=ALNI_MaNeiE4HKXHdLXSGXdDqeNWCOduJQ; Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1615685858,1615966588,1615984618,1615984669; Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=1615984669"}

    url = "https://www.liaoxuefeng.com/wiki/897692888725344/923029657876192"

    req = request.Request(url, headers=header)

    rsp = request.urlopen(req)

    print(type(rsp))  # 类型为 http.client.HTTPResponse
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("Info : {0}".format(rsp.info()))
    print("Code : {0}".format(rsp.getcode()))

    html = rsp.read()

    # cs = chardet.detect(html)
    # print(type(cs))
    # print(cs)
    # html = html.decode(cs.get("encoding", "utf-8"))
    html = html.decode()

    #print(html)




# 2. urllib
- 包含的模块
    - urllib.request: 打开和读取url
    - urllib.error: 包含urllib.request 产生的常见错误，使用try捕获
    - urllib.parse: 包含解析url的方法
    - urllib.robootparse: 解析roboots.txt 文件
    - 案例v1
    
- 网页编码问题解决
    - chardet  可以自动检测页面文件的编码格式，但是可能有误
    - 需要安装： conda install chardet
    - 案例v2

- urlopen 的返回对象
    - 案例v3
    - geturl：返回请求对象的url
    - info： 请求返回对象的

- request.data 的使用
    - 访问网络的两种方法
        - get ： 
            - 利用参数给服务器传递信息
            - 参数为dict, 然后使用parse编码
            - 案例v4
        - post： 
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post，需要使用data参数
            - 使用post 意味着http的请求可能需要更改
                - Content-Type： application/x-www.form-urlencode
                - Content-Length  数据长度
                - 简而言之， 一旦更改请求方法  请注意其他请求头部信息相适应
            - urllib.parse.urlencode 可以将字符串自动转换为上面的头信息
            - 案例v5
        
    
    
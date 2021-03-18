



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
            - 为了更多的设置请求信息，单纯通过urlopen函数已经不太好用了
            - 需要类用request.Request 类
            - 案例v6
        
- urllib.error
    - URLError产生的原因：
        - 没网
        - 服务器连接失败
        - 找不到指定服务器
        - 是OSError的子类
        - 案例v7
    - HTTPError  是URLError的一个子类
    
    - 两者区别：
        - HTTPError 是对应的HTTP请求的返回码错误，如果返回的是400以上，则引发HTTPError
        - URLEror 对应的一般是网络出现问题，包括url问题
        - 关系区别： OSError-URLError-HTTPError
        
- UesrAgent 用户代理 简称UA  属于headers的一部分  服务器通过UA来判断访问者身份(用更改UA来伪装自己的客户端身份)
    - 常见的UA值，使用的时候可以直接赋值粘贴，也可以用浏览器访问的时候抓包
    
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
            Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54

    - 设置UA可以通过两种方式：
        - heads
        - add_header
        - v9
    

- ProxyHander 处理（代理服务器）
    - 使用代理IP。是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidial.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问   代理也不允许频繁访问某一个固定网络，所以，代理一定要很多很多
    
    - 基本使用步骤
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener

- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半用户信息
    - 
- cookie & session的区别
    - 存放位置不同
    - cookie并不安全
    - session会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不会超过4K，很多浏览器限制一个站点最多保存20个
- session存放位置
    - 存在服务器
    - 一般情况下，session是放在内存中或者数据库中（绝大多数情况不用担心存放位置，django创建后台一般放在数据库）
    - 没有cookie登录  案例v11  可以看到  没有使用cookie 则返回的网页是未登录的状态

- 使用cookie登录
    - 直接把cookie复制下来， 然后手动放入请求头  案例v12
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie  向传出的http请求添加cookie
            - cookie存储在内存中  CookieJar实例回收后Cookie将消失
        - FileCookieJar（filename,delayload=None,policy=None）:
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar（filename,delayload=None,policy=None）
            - 创建与mozilla浏览器cookie.txt 兼容的FileCookieJar实例
        - LwpCookieJar（filename,delayload=None,policy=None）
            - 创建与libwww-perl 标准兼容的Set-Cookie3格式的FIleCookieJar实例
        - 他们的关系  CookieJar-FileCookieJar-MozillaCookieJar
    - 利用cookiejar 访问人人  案例13
        - 自动使用cookie登录，大致流程是：
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面
    - handler是Handler类的实例，常用参看案例代码
        - 用来处理复杂请求
            
            # 生成cookie的管理器
            cookie_handler = request.HTTPCookieProcessor(cookie) (cookie 是cookie = cookiejar.CookieJar())
            # 创建http请求管理器
            http_handler = request.HTTPHandler()
            # 生成https管理器
            https_handler = request.HTTPSHandler()
    - 创建handler后，使用opener打开， （专门负责打开），打开后相应的业务由相应的handler处理
    
    - cookie 作为一个变量打印出来  案例v14
        - cookie 属性
            - name: 名称
            - value值
            - domain ： 可以访问此cookie的域名
            - path ： 可以访问的cookie的页面路径
            - expires  过期时间
            - size  大小
            - Http  字段
    - cookie的保存-FileCookieJar  案例v15
    
    - cookie的读取，案例v16
    
- SSL
    - SSL证书就是指遵守SSL安全套接层协议的服务器数字证书，（SecureSocketLayer）
    - 美国网警公司开发
    - CA（CertifacateAuthority）是数字证书认证中心，是发放，管理，废除数字证书的手信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理   案例v17
    - 其实目前ssl.create_default_https_context = ssl._create_unverified_context
    - 已经不适用了  
    - 可以直接ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE 这样代替
        
- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是md5值）
    - 加密函数或者过程一定在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟除加密过程，从而达到破解
    - 案例v18   v19
    - 过程比较啰嗦   笔记较少  仔细观察
    
    r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
    



    
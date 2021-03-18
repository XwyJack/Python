# Django 系统
- 环境
    - Python 3.8
    - django 1.8
-参考资料
    - [django中文教程](python.uusyiyi.cn)
    - django 架站的16节课

- conda使用

# 环境搭建
- anaconda + pycharm
- anaconda使用
    - conda list: 显示当前环境安装的包
    - conda env list：显示安装的虚拟环境列表
    - conda create -n env_name python=3.8
    - (base) 是默认的虚拟环境
    - 激活conda的虚拟环境
        - （Linux） source activate  env_name
        - (windows)  conda activate env_name
    - pip install django=1.8
    



# 后台需要的流程

# 创建第一个django程序
- 命令行启动

        django-admin startproject wanyix
        cd wanyix
        python manage.py runserver
        
- pycharm 启动
    - 需要配置(添加interpreter)  找到刚创建的anaconda的虚拟环境的路径下的wanyix环境-python.exe就可以

# 路由系统-urls
- 创建app
    - app：负责具体业务或者一类具体业务的模块
    - python manage.py starteapp teacher
- 路由
    - 按照具体请求的url，导入到相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本上是接收的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用了RE
    - URL的具体格式为urls.py所示
- 需要关注两点：
    1. 接受的URL是什么，即如何使用RE对传入URL进行匹配
    2. 已知URL匹配到哪个处理模块
    
- url 匹配规则：
    - 从上往下一个一个比对
    - url格式是分级格式，则按照级别一级一级往下比对,主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url（比到子url，不会再往主url比对）
         - /one/two/three/
    - 正则以r开头,表示不需要转义，注意尖号(^)和美元符号($)
        - /one/two/three 能匹配到 r'^one/   路由会自动把/过滤掉
        - /oo/one/two/three 匹配不到 r'^one/"
        - /one/two/three/ 匹配到 r'three/$'
        - /oo/one/two/three/oo/ 匹配不到 r'three/$"
        - 开头不需要有反斜杠(路由会自动把/过滤掉)
    - 如果从上向下都没有找到合适的匹配内容，则报错

# 2. 正常映射 
- 把某一个符合RE的URL映射到事物处理函数中去
    - 举例如下:
    
    
        from showeast import views as sv

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap/', sv.normalmap),
        ]
        
# 3. URL中带参数映射
- 在事件处理代码中需要由URL传入参数,形如 /myurl/param中的param
- 参数都是字符串形式,如果需要整数等形式需要自行转换
- 通常的形式如下：
        
        ''''
             /search/page/432 中的 432需要经常性变换，所以设置成参数比较合适 
        '''
        
- url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam), 正则一定要写对，要不然就会报错404


# 4. URL在app中处理
- 如果所有应用URL都集中在wanyix/urls.py中，可能导致文件的臃肿
- 可以把urls具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入include
    - 注意此时RE部分的写法
    - 添加include导入
- 使用方法
    - 确保inclue被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数
- 同样可以使用参数
    
# 5. URL中的嵌套参数
- 捕获某个参数的一部分
    - 例如URL  /index/page-3  需要捕获数字3作为参数
    
    
        '''
            
        '''
    
# 6. 传递额外参数
- 参数不仅仅来自URL，还可能是我们自己定义的一个内容
    
        '''
        url(r'^yourname/$',tv.extraParam,{"name":"wanyix"})
        '''
- 附加参数同样使用于include语句，此时对include内所有都添加

# 7. URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后再编码代码中使用URL的值， 原则上都应该使用反向解析


# views视图

# 1. 视图概述
- 视图即视图函数，接收web请求并返回web响应的事物处理函数
- 相应符合http协议要求的任何内容，包括json string  html等
- 本章忽略事务处理，重点反放在如何返回处理结果中
# 2. 其它啊简单视图
- django.http 给我们提供了很多和HttpResponse类似的简单视图
通过查看django.http代码我们可以知道
- 此类使用方法基本类似，可以通过return语句直接返回给浏览器
- Http 404 为Exception的子类  所以需要raise使用

# 3. HttpResponse 详解
- 方法
    - init：使用页内同实例化HttpResponse对象
    - write（content）：以文件的方式写
    - flush（）：
    - set_cookie(key, value=' ', max_age=None, expires=None):设置cookie
        - key value 都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或timedate对象，会话将在指定的日期后过期
        - max_age和expires 二选一
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key):删除指定key的cookie，如果key不存在  则什么都不发生

# 4. HttpResponseRedict
- 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向地址
- 案例 ShowViews/views.py



# 5. Request 请求
- Request 介绍
    - 浏览器自动添加http头，然后向服务器发送的是http包文，此时还没有创建http的对象
    - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
    - 看request.py的源码
- 属性
    - 下面除非特别说明，属性都只是只读的
    - path：一个字符串，表示请求页面的完整路径，不包含域名
    - method：一个字符串 表示请求使用的HTTP方法   常用 “GET”  "POST"
    - encoding
    
    - GET: 一个类似字典的对象，包含get请求方式的所有参数
    - PUT：一个类似字典的对象， 包含post请求方式的所有参数
    - FILES： 一个类似字典的对象  包含所有上传的文件
    - COOKIES：一个标准的python字典包含所有cookie  键和值都为字符串
    - session： 一个既可读又可写的类似字典的对象， 表示当前会话
        - 只有当django 启用会话的支持时才可用
        - 详细内容见状态保持
- 方法：
    - is_ajax():（很重要） 如果请求是通过XMLHttpResponse发起的  则返回True  （什么是ajax  VUE  ORM）
    
    
- QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性都是GET  POST都是QueryDict类型的对象
    - 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
    - 方法get（） : 根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist（）：根据键获取值
            - 将键的值以列表形式返回，可以获取一个键的多个值
-GET属性
    - QueryDict类型的对象  http://127.0.0.1:8000/v8/?k1=wanyix&k2=xu&org=aws
    - 包含get请求方式的所有参数
    - 与url请求地址中的参数对应，位于？后面
    - 参数的格式是键值对  如key1 = value1
    - 多个参数之间使用&连接，如key1=value1&key2=value2
    - 键是开发人员定下来的  值是可变的
    - 案例/views/v8_get
    
- POST属性
    - QueryDict 类型的对象
    - 包含post请求方式的所有参数
    - QueryDict类型的对象
    - 包含post请求方式的所有参数
    - 与form表单中的控件对应
    - 表单中空间必须有name属性，name为键，value为值
        - checkbox存在一键多值的问题
    - 键是开发人员定下来的，值是可变的
    - 案例/views/v9_post
        - settings中设置模板位置(已经设置完毕)
        - 设置get页面的urls和函数
        
                # east/urls.py
                # 需要在路由文件中添加两个路由
                url(r'^v9_get/', views.v9_get),
                url(r'^v9_post/', views.v9_post),
                
                # ShowViews/views.py
                # 在文件中添加下面两个处理函数
                def v9_get(request):
                return  render_to_response("for_post.html")

                def v9_post(request):
                    rst = ""
                    for k,v in request.POST.items():
                        rst += k + "-->" + v
                        rst += ","

                    return HttpResponse("Get value of POST is {0} ".format(rst))
        - 添加文件/east/templates/for_post.html
        - 由于安全原因，需要在设置中安全选项中删除csrf设置


                # settings.py
  

                MIDDLEWARE = [
                    'django.middleware.security.SecurityMiddleware',
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.middleware.common.CommonMiddleware',
                    #  下面这句话被注释掉
                    #'django.middleware.csrf.CsrfViewMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                ]

- 手动编写视图：
    - 实验目的:
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理

    - 分析：
        - django把所有请求信息封装进request
        - django通过urls模块把相应请求跟事件处理函数链接起来, 并把request作为参数传入
        - 在相应的处理函数中,我们需要完成两部分
            - 处理业务
            - 把结果封装并返回,我们可以使用简单HttpResponse,同样也可以自己处理此功能,例如我们本例需要做的
        - 本案例不介绍业务处理,把目光集中在如何渲染结果并返回
    -render(request, template_name[, context][, context_instance][, content_type][, status][, current_app][, dirs][, using])
        - 使用模板和一个给定的上下文环境,返回一个渲染和的HttpResponse对象
        - request: django的传入请求
        - template_name: 模板名称
        - content_instance: 上下文环境
        - 案例参看代码 teacher_app/views/render_test
    - render_to_response
        - 根据给定的上下文字典渲染给定模板,返回渲染后的HttpResponse
        
        
        
        
- 系统内建视图
    - 系统内建视图，可以直接使用
    - 404
        - default.page_not_found(request, template_name='404.html')
        - 系统引发Http404时出发
        - 默认船体request_path变量给模板,即导致错误的URL
        - DEBUG=True则不会调用404, 取而代之是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量(MEDIA_URL等)
    - 500(server error)  
        - defaults.server_error(request, template_name='500.html')
        - 需要DEBUG=False,否则不调用
    - 403 (HTTP Forbidden) 视图   
        - defaults.permission_denied(request, template_name='403.html')
        - 通过PermissionDenied触发
    - 400 (bad request) 视图
        - defaults.bad_request(request, template_name='400.html')
        - DEBUG=False
        
        
        
        
        
        

# Models  模型

- 数据结构（数据的结构化存储） + 算法 = 程序
    - ORM
        - ObjectRelationMap: 把面向对象思想转换成关系型数据库
        - 类对应表格
        - 类中的属性对应表中的字段
        - 在应用中的models.py文件中定义class
        - 所有需要使用ORM的class都必须是models.Model的子类
        - class中的所有属性对应表格中的字段
        - 字段的类型都必须使用models.xxxx    不能使用python中的类型
        - 在django中， Models负责跟数据库交互
- django 连接数据库
    - 自带默认数据 Sqllite3
        - 关系型数据库
        - 轻量级
    - 建议开发用sqlit3   部署的时候使用mysql之类数据库
        - 切换数据库在settings中进行设置
    
                django 连接 mysql
                    DATABASES = [ 
                        'default' = { 
                            'ENGINE' : 'django.db.backends.mysql', 
                            'NAME' : '数据库名', 
                            'PASSWORD': '数据库密码', 
                            'HOST': '127.0.0.1', 
                            'PORT': '3306', } ]

        - 需要在项目文件下的__init__文件中导入pymysql包



# models类的使用
- 定义数据库表映射的类
    - 在应用的models.py文件中定义cLass
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用models.xxxx    不能使用python中的类型
- 字段常用参数：
    1. max_length
    2. blank
    3. null
    4. default
    5. unique
    6. verbose_name
    
- 数据库的迁移
    1. 在命令行中，生成数库迁移的语句（生成sql语句）
        
        '''
        python3 manage.py  makemigrations
        '''    
    2. 在命令行中， 输入数据库迁移的指令
    
        '''
        python3 manage.py  migrate
        '''
        
        ps: 
    3.  对于默认数据库， 为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把系统 自带的sqlite3数据库删除


## 1. 查看数据库中的数据

            1. 启动命令行 : python3 manage.py shell
            ps: 注意点: 对orm的操作分为静态函数和非静态函数两种.静态是指在内存中只有一份内容存在,调用的时候使用 类名. 的方式.如果修改了那么所有使用的人都会受影响.
            2. 在命令行中导入对应的映射类
	            from 应用.models import 类名
            3. 使用 objects 属性操作数据库. objects 是 模型中实际和数据库进行交互的 Manager 类的实例化对象.
            4. 查询命令
	            - 类名.objects.all() 查询数据库表中的所有内容. 返回的结果是一个QuerySet类型,实际上是类列表中装这个一个一个数据对象.
	            - 类名.objects.filter(条件) 
        
        
----------------------

            # from 应用名.models import 类名
            from myapp.models import Student

            # 查询Student表中的所有数据,得到的是一个QuerySet类型
            Student.objects.all()

            # 如果要取出所有QuerySet类型中的所有数据对象,需要遍历取出所有的对象,再用对象.属性来查看值
            s = Student.object.all()
            for each in s:
	            print(each.name , each.age , each.address , each.phone)

            # 如果要进行过滤筛选,使用filter()方法
            Student.objects.filter(age=18)

-----------------------

## 2. 添加数据

- 对象 = 类()   # 使用类实例化对象
- 对象.属性 = 值  # 给对应的对象的属性赋值
- 对象.save()  # 必须要执行保存操作,否则数据没有进入数据库

- python3 manage.py shell 命令行中添加数据

            # from 应用名.models import 类名

            from myapp.models import Student

            # 实例化对象
            s = Student()
            
            # 给对象的属性赋值
            s.name = '张三'
            s.address = '云南昭通'
            s.phone = '13377886678'
            s.age = 20
            
            # 保存数据
            s.save()
            
- 常见查找方法
    - 1.通用查找格式: 属性名 _ _ (用下面的内容) =值
        gt : 大于
        gte : 大于等于
        lt : 小于
        lte : 小于等于
        range: 范围
        year : 年份
        isnull : 是否为空
    - 2.查找等于指定值的格式: 属性名 = 值
    - 3.模糊查找: 属性名 _ _ (使用下面的内容) = 值
        exact : 精确等于
        iexact: 不区分大小写
        contains: 包含
        startwith: 以..开头
        endwith: 以…结尾 
        
        
# 数据库表关系





























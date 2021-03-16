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
-  
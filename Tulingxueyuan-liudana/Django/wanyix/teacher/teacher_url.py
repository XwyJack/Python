from django.conf.urls import include, url
# 从主路由导入子路由  需要include
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wanyix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 下面的路由就是一个包含两个参数的函数
    # 视图函数名称只有名称，无括号和参数
    url(r'wanyix/', views.do_app),

]

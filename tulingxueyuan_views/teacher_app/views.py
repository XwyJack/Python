from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.core.urlresolvers import reverse


# 按ctrl 然后点上面的http 就会发现许多定义好的视图
# HttpResponse 作为标准的http的返回

# Create your views here.


def teacher(request):
    return HttpResponse("This is a teacher view")

# 如果retun后面多加了 逗号，就会报错 'tuple' object has no attribute 'get'


def v2_exception(r):

    raise Http404
    return HttpResponse("OK")
    # 返回httpresponse 以ok作为参数
    # You're seeing this error because you have DEBUG = True in your Django settings file.
    # Change that to False, and Django will display a standard 404 page.
    # 在setting中设置  DEBUG = False 和 ALLOWED_HOSTS = ["127.0.0.1"]
    # 正常就应该是true


def v10_1(request):
    return HttpResponseRedirect("/v11")


def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))


def v11(request):
    #return HttpResponseRedirect("hh,This is the v11's response.")
    return HttpResponse("hh,This is the v11's response.")


def v8_get(requset):
    rst = ""
    for k, v in requset.GET.items():
        rst += k + "--->" + v
        rst += ","
    return HttpResponse("Get the value of Request is {0}".format(rst))


def v9_get(request):
    # 渲染
    return render_to_response("for_post.html")


def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "--->" + v
    return HttpResponse("Get the value of Request is {0}".format(rst))


# 手动处理视图
def render_test(request):

    # 环境变量
    # c = dict()
    rsp = render(request, "render.html")
    # rsp = HttpResponse(request, "render.html")
    return rsp


# 手动写一个dict
def render2_test(request):

    # 环境变量
    c = dict()
    c["name"] = "wanyix"
    # 上面怎么用值wanyix替换name这个环境变量，这是模板干的活  肯定能干

    c["name2"] = "wanyix2"
    c["name3"] = "wanyix3"

    rsp = render(request, "render2.html", context=c)
    return rsp


def render3_test(request):
    # 视图函数的返回必须是response的子类
    from django.template import loader

    # 得到模板
    t = loader.get_template("render2.html")
    print(type(t))
    r = t.render({"name": "wanyixxx"})
    print(type(r))

    return HttpResponse(r)


def render4_test(request):

    # 加载render2.html
    # render_to_response 不受用
    rsp = render_to_response("render2.html", context={"name": "wanyixxxxxx"})

    return rsp


def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request, template_name="render.html")
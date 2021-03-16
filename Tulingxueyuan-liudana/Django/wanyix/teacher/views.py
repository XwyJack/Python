from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse

# Create your views here.

'''
视图函数需要一个参数，类型应该是 HttpRequest
'''


def do_normalmap(request):
    print("In do_normalmap")
    return HttpResponse("This is normalmap")


def withparam(request, year, month):
    print("error?")
    return HttpResponse("This is with param {0}, {1}".format(year, month))


def do_app(request):
    return HttpResponse("This is a sub route")


def do_param2(request,pn):
    return HttpResponse("Page number is {0}".format(pn))


def extraParam(request, name):
    return HttpResponse("My name is {0}".format(name))


def revParse(request):
    return HttpResponse("Your request URL is {0}".format(reverse("askname")))
# 上面reverse后面的名称要用“ ”括起来

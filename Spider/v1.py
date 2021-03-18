from urllib import request

'''
使用urllib.request 请求一个网页内容，并把内容返回
'''


if __name__ == '__main__':
    url = "https://study.163.com/course/courseLearn.htm?courseId=1210561804&share=1&shareId=1458210960#/learn/live?lessonId=1281822211&courseId=1210561804"
    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))
    html = html.decode()

    print(html)


'''
定义一个学生类，用来形容学生

'''


class Student():
    # 一个空类  pass表示占位 代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
wanyix = Student()


# 再定义一个类，用来描述学Pyton的学生

class PythonStudent():
    # 用None给不确定的赋值
    name = None
    age = 18
    course = "Python"

    #需要注意
    # 1 def doHomework的缩进层级  跟变量一个层级
    # 2 系统默认有个self参数
    def doHomework(self):
        print("I do the homework")
        # 在函数末尾使用return语句
        return None

#  实例化一个叫wanyix的学生  是一个具体的人


wanyix = PythonStudent()
print(wanyix.name)
print(wanyix.age)


# 注意  成员函数的调用没有传递进参数
wanyix.doHomework()

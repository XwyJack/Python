# 包含一个学生类
# 一个sayHello函数
# 一个打印语句

class Student():
    def __init__(self,name = "NoName", age = 29):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi,welcome to here!")

print("I am the module p01.")

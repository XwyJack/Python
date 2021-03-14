# 包含一个学生类
# 一个sayHello函数
# 一个打印语句

class Student():
    def __init__(self, name="NoName", age=29):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi,welcome to here!")


# 当文件作为import的时候，底下不是main，不执行
# 此判断语句建议一直作为程序的入口


if __name__ == '__main__':
    print("I am the module p01.")
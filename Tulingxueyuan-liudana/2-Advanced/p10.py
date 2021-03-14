from pkg02 import *

stu = p01.Student()

stu.say()


# init()  #NameError: name 'init' is not defined  因为pkg02 中__init__.py中有__all__ 内容指定了p01， 所以不能调用init中的内容


"""
继承介绍:
    概述:
        现实中的继承指的是: 子承父业, 编程中的继承指的是: 子类从父类继承过来 属性 和 行为.
    格式:
        class 子类名(父类名):
            pass
    例如:
        class A(B):
            pass
    叫法:
        类A: 子类, 派生类, 扩展类.
        类B: 父类, 基类, 超类.
    好处:
        提高代码的复用性.
    细节:
        所有的类都直接或者间接继承自 object类, 它是所有类的父类, 基类.
"""


# 1.定义father类，充当父类
class Father(object):
    def __init__(self):
        self.gender = '男'

    def walk(self):
        print('活到99岁!')


# 2.定义son类，充当子类
class Son(Father):      # Son继承于Father  Father继承于object
    pass



# 3.在main中测试
if __name__ == '__main__':
    s = Son()
    print(s.gender)
    s.walk()

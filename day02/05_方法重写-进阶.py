"""
案例: 演示 方法重写后, 子类如何调用父类的 行为(函数)

问题: 重写后, 子类 如何访问 父类的成员?
答案:
    方式1: 父类名.父类方法名(self)            # self本类当前对象的引用.
    方式2: super().父类方法名()

super 关键字介绍:
    概述:
        它代表 本类当前对象 父类的引用.
    简单理解:
        self 代表自己,  super 代表父类.
    细节:
        1. super()只能初始化第1个父类的成员, 所以 super写法 不适用于 多继承, 更适用于 单继承.
        2. 在单继承关系中, 可以把 super().父类方法名(self) 简写成 super().父类方法名()
        3. 多继承关系中, 如果想精准的初始化某个父类的成员, 要通过 父类名.父类方法名(self) 的方式实现.
"""

# 需求4: 很多顾客都希望吃到 徒弟自研的煎饼果子, 也有 黑马配方的煎饼果子味道. 请用所学, 模拟这个知识点.

# 1. 定义师傅类Master.
class Master(object):
    # 1.1 属性, kongfu = '[古法摊煎饼果子技术]'
    def __init__(self):
        self.kongfu = '[古法摊煎饼果子技术]'

    # 1.2 行为, make_cake(), 表示: 摊煎饼.
    def make_cake(self):
        print(f'采用 {self.kongfu} 制作煎饼果子!')


# 2. 定义黑马学校类School.
class School(object):
    # 2.1 属性, kongfu = '[黑马AI摊煎饼果子技术]'
    def __init__(self):
        self.kongfu = '[黑马AI摊煎饼果子技术]'

    # 2.2 行为, make_cake(), 表示: 摊煎饼.
    def make_cake(self):
        print(f'采用 {self.kongfu} 制作煎饼果子!')


# 3. 定义徒弟类Prentice, 继承自 师傅类.
class Prentice(School, Master):  # 多继承, 同名属性和行为, 优先参考第1个父类, 即: 从左往右的顺序.
    # 3.1 属性
    def __init__(self):
        self.kongfu = '[独创(自研) 摊煎饼果子技术]'

    # 3.2 行为, make_cake(), 表示: 摊煎饼.
    def make_cake(self):
        print(f'采用 {self.kongfu} 制作煎饼果子!')

    # 3.3 行为，从老师傅继承的煎饼果子配方 make_master_cake()
    def make_master_cake(self):
        # 子类调用父类行为, 方式1: 父类名.父类方法名(self)
        # 初始化父类的 属性, 即: 调用父类的 __init__()函数
        Master.__init__(self)   # 等价于做了: self.kongfu = '[古法摊煎饼果子技术]'
        Master.make_cake(self)  # 调用父类的行为.

    # 3.4 行为，从学校继承的煎饼果子配方 make_master_cake()
    def make_school_cake(self):
        # 子类调用父类行为, 方式1: 父类名.父类方法名(self)
        # 初始化父类的 属性, 即: 调用父类的 __init__()函数
        School.__init__(self)  # 等价于做了: self.kongfu = '[黑马AI摊煎饼果子技术]'
        School.make_cake(self)  # 调用父类的行为.

    # 3.5 行为，旧的煎饼果子配方 make_old_cake()
    def make_old_cake(self):
        # 子类调用父类行为, 方式2: super().父类方法名()
        super().__init__()  # 初始化父类的成员.
        super().make_cake()


# 在main函数中测试.
if __name__ == '__main__':
    # 4. 创建徒弟类对象.
    p = Prentice()
    print(p.make_cake())
    # 5. 打印 徒弟类对象 从Master()父类继承过来的 行为.

    # 6. 打印 徒弟类对象 从School()父类继承过来的 行为.

    # 7. 打印 徒弟类对象 从父类继承过来的 行为. 即：旧的煎饼果子配方



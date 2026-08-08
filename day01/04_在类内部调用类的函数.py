"""
案例:
    演示 在类内部, 通过 self关键字, 访问类内部(自己的) 函数.

细节:
    在类中调用 类的行为(函数), 可以通过 self.的方式 调用.
"""


# 需求: 定义汽车类, 其有 run() 和 work()两个函数, run()表示跑的功能, 在work()函数中调用run()函数, 并在main方法中, 创建对象, 调用并测试.
class Car():
    def run(self):
        print('我是 run 函数!')
        print('汽车会跑哦!')
        print('-' * 30)

    def work(self):
        print('我是 work 函数!')
        self.run()                  # 类内部可以通过self.的方式调用


if __name__ == '__main__':
    c1 = Car()
    c1.run()
    c1.work()

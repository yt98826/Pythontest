"""
self关键字介绍:
    概述:
        它代表本类当前对象的引用, 一般用于: 函数中, 即: 谁调用这个函数, self就代表谁(哪个对象).
    简单记忆:
        谁(本类对象)调用(函数), self就代表谁.

"""

# 需求1：创建汽车类Car，并创建两个对象，观察结果
class Car:
    def run(self):
        print('car can run')
        print(f'self: {self}')


if __name__ == '__main__':
    # 创建对象
    car1 = Car()
    car2 = Car()

    # 调用类的成员
    car1.run()
    car2.run()

    # 打印对象名
    print(car1)        # <__main__.Car object at 0x000002C38F31D790>
    print(car2)        # <__main__.Car object at 0x000002C38F31D7C0>

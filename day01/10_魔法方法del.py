"""
概述：
    当删除对象时，Python解释器也会默认调用__del__()方法.
    __del__(self)    析构器，当一个实例被销毁时调用的方法
"""

class Car():
    def __init__(self, color, number):      # 这里的两个参数可以是其他名称，但最好要见名知意
        self.color = color                  # self.color 这里是 把用户传递的参数用于添加属性
        self.number = number

    # 魔法方法 __str__() 输出语句print打印对象时，会自动调用，一般用于打印对象的各个属性值
    def __str__(self):
        return '看我返回了什么: ' + str(self.color) + ' ' + str(self.number)
        # return f'{self.color}的汽车有{self.number}个车轮'

    def __del__(self):
        print('我在这里自动调用了魔法方法 __del__() 哦!')


if __name__ == '__main__':
    c1 = Car('brown', 5)    # 这里如果不传参数就会报错
    print(f'汽车颜色：{c1.color}, 汽车轮胎：{c1.number}')
    print(c1)
    print('-' * 30)

    c2 = Car('猛男粉', 78)
    print(c2)
    print('*' * 30)

    # del c1    # 我在这里自动调用了魔法方法 __del__() 哦!   这里相当于自动删除了c1
    # del c2

"""
概述：
    当使用print输出对象时，默认打印对象的内存地址值【十六进制】.
    若要让输出打印对象名时，得到的结果不是内存地址值，应该要在类中定义str方法.
    如果类定义了__str__方法，那么就会打印存在这个方法中 return的数据。
格式：
    class 类名:
        def __str__(self):
            代码
            ...
        return 值        # 说明:值的类型必须是字符串类型
"""

class Car():
    def __init__(self, color, number):      # 这里的两个参数可以是其他名称，但最好要见名知意
        self.color = color                  # self.color 这里是 把用户传递的参数用于添加属性
        self.number = number

    # 魔法方法 __str__() 输出语句print打印对象时，会自动调用，一般用于打印对象的各个属性值
    def __str__(self):
        return '看我返回了什么: ' + str(self.color) + ' ' + str(self.number)
        # return f'{self.color}的汽车有{self.number}个车轮'


if __name__ == '__main__':
    c1 = Car('brown', 5)    # 这里如果不传参数就会报错
    print(f'汽车颜色：{c1.color}, 汽车轮胎：{c1.number}')
    print(c1)

    print('-' * 30)

    c2 = Car('猛男粉', 78)
    print(c2)

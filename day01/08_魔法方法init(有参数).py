"""
有参数的__init__()方法,当需要通过类外部传递相应变量值用于改变某些属性时,可以使用.格式如下：
    def __init__(self,参数1,参数2,...):
    代码
    ......
"""

# 需求：通过外部给车这个对象设置color(颜色)、number(轮胎数)值.

class Car():
    def __init__(self, color, number):      # 这里的两个参数可以是其他名称，但最好要见名知意
        self.color = color                  # self.color 这里是 把用户传递的参数用于添加属性
        self.number = number


if __name__ == '__main__':
    c1 = Car('brown', 5)    # 这里如果不传参数就会报错
    print(f'汽车颜色：{c1.color}, 汽车轮胎：{c1.number}')

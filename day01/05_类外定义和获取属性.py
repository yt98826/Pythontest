"""
案例: 演示在 类外定义 和 获取 属性.

格式:
    添加属性   对象名.属性名 = 属性值
    获取属性   对象名.属性名
"""

# 案例: 定义汽车类, 在类外给汽车对象 设置属性, 颜色=红色, 轮胎 = 4, 获取属性值并打印.

# 1.定义汽车类
class Car():
    # 定义 run 函数
    def run(self):
        print('车可以跑!')


if __name__ == '__main__':
    # 3.创建汽车类对象
    c1 = Car()

    # 4.调用行为
    c1.run()

    # 5.设置属性
    c1.name = '奔驰幻影'
    c1.color = 'Red'
    c1.num = 4

    # 6.获取属性
    print(f'名称: {c1.name}, 颜色: {c1.color}, 轮胎数: {c1.num}')
    print('-' * 30)

    # 7.用另一个汽车类的对象，测试有无上述属性
    c2 = Car()
    c2.run()
    # print(c2.num)         # 属性错误 AttributeError: 'Car' object has no attribute 'num'

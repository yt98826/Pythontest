"""
需求：
    减肥案例.
案例描述：
    小明同学当前体重是100kg[默认].

    每当他跑步一次时，则会减少0.5kg；

    每当他大吃大喝一次时，则会增加2kg。

    请试着采用面向对象方式完成案例。
分析：
    类：学生Student 类
        属性：
            体重  weight
        行为：
            跑步  run()
            吃   eat()
"""
# 1.定义学生类
class Person():
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        # return f'{self} 当前的体重是：{self.weight} kg'
        # 不要单独写self,会无限递归,可以在init里面添加姓名属性，再调用就避免了单独使用self
        return f'当前的体重是：{self.weight} kg'

    def run(self):
        self.weight -= 0.5
        print(f'当前的体重是：{self.weight} kg')

    def eat(self):
        self.weight += 2
        print(f'当前的体重是：{self.weight} kg')


if __name__ == '__main__':
    xiaoming = Person(100)
    print(xiaoming)
    xiaoming.run()
    xiaoming.eat()
    xiaoming.run()
    xiaoming.run()
    xiaoming.run()


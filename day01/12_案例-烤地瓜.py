"""
需求:
    定义一个 地瓜类, 属性为: 被烤的时间(cook_time), 地瓜的生熟状态(cook_state), 添加的调料(condiments).
    行为有: cook() 表示烘烤,  add_condiment() 表示 添加调料.
    请用所学, 用面向对象的思维完成这个事情.

烘烤规则(时间及其对应的状态):
    0 ~ 3分钟     生的
    3 ~ 7分钟     半生不熟
    7 ~ 12分钟    熟了
    超过12分钟     已烤焦, 糊了
"""

# 1.定义地瓜类
class Potato():
    # 2.定义init()，用来初始化属性
    def __init__(self):
        """
        init()魔法方法，用来初始化属性
        """
        self.cook_time = 0      # 烘烤时间
        self.cook_state = '生的'    # 地瓜状态
        self.condiments = []    # 添加的调料

    # 3.具体的烤地瓜方法，接收烘烤时间，根据时间调整烘烤状态
    def cook(self, time):
        # 3.1 非法值校验
        if time < 0 :
            print('烘烤时间非法，请重新传入!')
        else:
            # 3.2 走到这里，合法烘烤
            self.cook_time = self.cook_time + time
            # 3.3 判断烘烤状态
            if 0 <= self.cook_time < 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time < 7:
                self.cook_state = '半生不熟'
            elif 7 <= self.cook_time < 12:
                self.cook_state = '熟了'
            else:
                self.cook_state = '烤焦了'

    # 4.添加调料动作
    def add_condiment(self, condiment):
        self.condiments.append(condiment)   # 向列表中添加调料

    # 5.打印对象属性值
    def __str__(self):
        return f'烘烤时间为: {self.cook_time}, 烘烤状态为: {self.cook_state}, 添加的调料有: {self.condiments}'

# 6.main中的主要操作
if __name__ == '__main__':
    # 6.创建对象
    tudou = Potato()

    # 7.具体烘烤、添加调料动作
    tudou.cook(2)
    tudou.cook(5)
    tudou.add_condiment('辣椒酱')
    tudou.add_condiment('含笑半步癫')

    # 8.打印土豆状态
    print(tudou)
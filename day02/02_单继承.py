"""
单继承:
    类只能继承自另外的1个类, 从中继承过来 属性 和 行为.
"""

# 需求: 一个摊煎饼的老师傅, 研发了一套精湛的摊煎饼的技术. 他(老师傅)要传授这套技术给徒弟. 请用所学, 模拟这个知识点.
# 1.定义师傅类
class Master(object):
    def __init__(self):
        self.kongfu = ['板面', '焖子']


# 2.定义徒弟类
class Tudi(Master):
    pass


# 3.在main中测试
if __name__ == '__main__':
    tudi = Tudi()
    print(tudi.kongfu)

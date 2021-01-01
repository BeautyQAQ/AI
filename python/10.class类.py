# 类
class Calculator:       #首字母要大写，冒号不能缺
    name='Good Calculator'  #该行为class的属性
    price=18
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

    def __init__(self,name,price,hight=10,width=14,weight=16): #后面三个属性设置默认值
        self.name=name
        self.price=price
        self.h=hight
        self.wi=width
        self.we=weight
cal=Calculator()  #注意这里运行class的时候要加"()",否则调用下面函数的时候会出现错误,导致无法调用.
cal.add(10,20)
cal.minus(10,20)
# 注意这里的self 是默认值.

# class 类 init 功能
# 运行c=Calculator('bad calculator',18,17,16,15)
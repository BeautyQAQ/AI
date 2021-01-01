# zip 
# zip函数接受任意多个（包括0个和1个）序列作为参数，合并后返回一个tuple列表
a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))  #需要加list来可视化这个功能

# zip 中的运算
a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
     print(i/2,j*2)


# lambda 
# fun = lambda x,y : x+y, 冒号前的x,y为自变量，冒号后x+y为具体运算
fun= lambda x,y:x+y
x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
y=int(input('y='))
print(fun(x,y))


# map
# map是把函数和参数绑定在一起
def fun(x,y):
    return (x+y)
list(map(fun,[1],[2]))
# while循环
# 比如要打印出 0 - 9 的所有数据
condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1
# 在使用 while 句法的时候一定要注意在循环内部一定要修改判断条件的值，否则程序的 while 部分 将永远执行下去。
# while True:
#     print("I'm True")
# 如果这样做的话，程序将一直打印出 I'm True, 要停止程序，使用 ctrl + c 终止程序。

# 整数和浮点数也能进行 Boolean 数据操作, 具体规则，如果该值等于 0 或者 0.0 将会返回 False 其余的返回 True
condiiton = 10
while condiiton:
    print(condiiton)
    condiiton -= 1

# 如果 while 后面接着的语句数据类型 None, 将会返回 False。
# 在 Python 中集合类型有 list、 tuple 、dict 和 set 等，如果该集合对象作为 while 判断语句， 
# 如果集合中的元素数量为 0，那么将会返回 False, 否则返回 True。
a = range(10)
while a:
    print(a[-1])
    a = a[:len(a)-1]

# for循环
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
for i in example_list:
    print(i)

for i in example_list:
    print(i)
    print('inner of for')
print('outer of for')

# 1 range(start, stop) 其中 start 将会是序列的起始值，stop为结束值，但是不包括该值，类似 
# 数学中的表达 [start, stop),左边为闭区间，右边为开区间。

# 2 range(stop)
# 如果省略了 start 那么将从 0 开始，相当于 range(0, stop)

# 3 range(start, stop, step)
# step 代表的为步长，即相隔的两个值得差值。从 start 开始，依次增加 step 的值，直至等于或者大于 stop

# 集合
# tuple 类型  --  元组
tup = ('python', 2.7, 64)
for i in tup:
    print(i)

# dictionary 类型
dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key, dic[key])
# 注意字典中 key 是乱序的，也就是说和插入 的顺序是不一致的。
# 如果想要使用顺序一致的字典，请使用 collections 模块 中的 OrderedDict 对象。

# set 类型
s = set(['python', 'python2', 'python3','python'])
for item in s:
    print(item)
# set 集合将会去除重复项，注意输出的 结果也不是按照输入的顺序。


# 迭代器
# define a Fib class
# Python 中的 for 句法实际上实现了设计模式中的迭代器模式,所以我们自己也可以按照迭代器的要求自己生成迭代器对象,
# 以便在 for 语句中使用。只要类中实现了 __iter__ 和 next 函数，那么对象就可以在 for 语句中使用。
class Fib(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

# using Fib object
for i in Fib(5):
    print(i)


# 4.3 生成器
# 除了使用迭代器以外，Python 使用 yield 关键字也能实现类似迭代的效果，yield 语句每次执行时，
# 立即返回结果给上层调用者，而当前的状态仍然保留，以便迭代器下一次循环调用。
# 这样做的 好处是在于节约硬件资源，在需要的时候才会执行，并且每次只执行一次。
def fib(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a+b
        max -= 1
        yield r

# using generator
for i in fib(5):
    print(i)
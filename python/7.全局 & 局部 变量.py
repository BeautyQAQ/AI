# 局部变量
def fun():
    a = 10
    print(a)
    return a+100
print(fun())

# 全局变量
APPLE = 100 # 全局变量
a = None
def fun():
    global a    # 使用之前在全局里定义的 a
    a = 20      # 现在的 a 是全局变量了
    return a+100

print(APPLE)    # 100
print('a past:', a)  # None
fun()
print('a now:', a)   # 20
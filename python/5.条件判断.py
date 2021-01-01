# if 判断
x = 1
y = 2
z = 3
if x < y:
    print('x is less than y')
if x < y < z:
    print('x is less than y, and y is less than z')
# 注意上面这行这个用法是 python 语言特有，不鼓励 大家写出这样的代码
x = 2
y = 2
z = 0
if x == y:
    print('x is equal to y')

# if else
x = 1
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal to y')


# python 中并没有类似 condition ? value1 : value2 三目操作符,python 可以通过 if-else 的行内表达式完成类似的功能。
# var = var1 if condition else var2
# 可以这么理解上面这段语句，如果 condition 的值为 True, 那么将 var1 的值赋给 var;如果为 False 则将 var2 的值赋给 var。
worked = True
result = 'done' if worked else 'not yet'
print(result) # 输出 done

# if elif else 判断
x = 4
y = 2
z = 3
if x > 1:
    print ('x > 1')
elif x < 1:
    print('x < 1')
else:
    print('x = 1')
print('finish')
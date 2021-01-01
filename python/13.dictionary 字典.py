# dictionary 字典
a_list = [1,2,3,4,5,6,7,8]

d1 = {'apple':1, 'pear':2, 'orange':3}
d2 = {1:'a', 2:'b', 3:'c'}
d3 = {1:'a', 'b':2, 'c':3}

print(d1['apple'])  # 1
print(a_list[0])    # 1

del d1['pear']
print(d1)   # {'orange': 3, 'apple': 1}

d1['b'] = 20
print(d1)   # {'orange': 3, 'b': 20, 'apple': 1}

# 字典存储类型
def func():
    return 0

d4 = {'apple':[1,2,3], 'pear':{1:3, 3:'a'}, 'orange':func}
print(d4['pear'][3])    # a
# 字典还可以以更多样的形式出现，例如字典的元素可以是一个List，或者再是一个列表，再或者是一个function
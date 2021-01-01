# Tuple
# 用小括号、或者无括号来表述，是一连串有顺序的数字
a_tuple = (12, 3, 5, 15 , 6)
another_tuple = 12, 3, 5, 15 , 6

# List
# list是以中括号来定义的
a_list = [12, 3, 67, 7, 82]

# 两者对比
# 他们的元素可以一个一个地被迭代、输出、运用、定位取值:
for content_tuple in a_tuple:
    print(content_tuple)
for content in a_list:
    print(content)

for index in range(len(a_list)):
    print("index = ", index, ", number in list = ", a_list[index])
for index in range(len(a_tuple)):
    print("index = ", index, ", number in tuple = ", a_tuple[index])

# List 添加
# 列表是一系列有序的数列，有一系列自带的功能
a = [1,2,3,4,1,1,-1]
a.append(0)  # 在a的最后面追加一个0
print(a)
# [1, 2, 3, 4, 1, 1, -1, 0]

a = [1,2,3,4,1,1,-1]
a.insert(1,0) # 在位置1处添加0
print(a)
# [1, 0, 2, 3, 4, 1, 1, -1]


# List 移除
a = [1,2,3,4,1,1,-1]
a.remove(2) # 删除列表中第一个出现的值为2的项
print(a)
# [1, 3, 4, 1, 1, -1]


# List 索引
a = [1,2,3,4,1,1,-1]
print(a[0])  # 显示列表a的第0位的值
# 1

print(a[-1]) # 显示列表a的最末位的值
# -1

print(a[0:3]) # 显示列表a的从第0位 到 第2位(第3位之前) 的所有项的值
# [1, 2, 3]

print(a[5:])  # 显示列表a的第5位及以后的所有项的值
# [1, -1]

print(a[-3:]) # 显示列表a的倒数第3位及以后的所有项的值
# [1, 1, -1]


# List 排序
a = [4,1,2,3,4,1,1,-1]
a.sort() # 默认从小到大排序
print(a)
# [-1, 1, 1, 1, 2, 3, 4, 4]

a.sort(reverse=True) # 从大到小排序
print(a)
# [4, 4, 3, 2, 1, 1, 1, -1]


# 多维列表
# 创建二维列表   一个一维的List是线性的List，多维List是一个平面的List
a = [1,2,3,4,5] # 一行五列
multi_dim_a = [[1,2,3],
               [2,3,4],
               [3,4,5]] # 三行三列

# 索引
print(a[1])
# 2

print(multi_dim_a[0][1])
# 2
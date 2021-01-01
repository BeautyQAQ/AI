# Numpy 索引
import numpy as np

# 一维索引
A = np.arange(3,15)

# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
         
print(A[3])    # 6

A = np.arange(3,15).reshape((3,4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""
# 这时的A[2]对应的就是矩阵A中第三行(从0开始算第一行)的所有元素
print(A[2])         
# [11 12 13 14]


# 二维索引
print(A[1][1])      # 8
print(A[1, 1])      # 8
# 在Python的 list 中，我们可以利用:对一定范围内的元素进行切片操作，在Numpy中我们依然可以给出相应的方法：
print(A[1, 1:3])    # [8 9]  这一表示形式即针对第二行中第2到第4列元素进行切片输出（不包含第4列）
for row in A:
    print(row)
"""    
[ 3,  4,  5, 6]
[ 7,  8,  9, 10]
[11, 12, 13, 14]
"""

# 逐列打印
for column in A.T:
    print(column)
"""  
[ 3,  7,  11]
[ 4,  8,  12]
[ 5,  9,  13]
[ 6, 10,  14]
"""



# 迭代输出的问题
A = np.arange(3,15).reshape((3,4))
         
print(A.flatten())   
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)
# 这一脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。而flat是一个迭代器，本身是一个object属性。
# 3
# 4
# ……
# 14
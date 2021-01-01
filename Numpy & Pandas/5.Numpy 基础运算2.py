# Numpy 基础运算2
import numpy as np
A = np.arange(2,14).reshape((3,4)) 

# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])
# 元素的索引  
print(np.argmin(A))    # 0
print(np.argmax(A))    # 11

# 均值
print(np.mean(A))        # 7.5
print(np.average(A))     # 7.5
# mean()函数还有另外一种写法：
print(A.mean())          # 7.5
# 中位数的函数
print(np.median(A))       # 7.5

# 和matlab中的cumsum()累加函数类似，Numpy中也具有cumsum()函数，其用法如下：
print(np.cumsum(A)) 
# [2 5 9 14 20 27 35 44 54 65 77 90]
# 累差运算函数：
print(np.diff(A))  
# nonzero()函数：
print(np.nonzero(A))    
# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))
# 这个函数将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。

import numpy as np
A = np.arange(14,2, -1).reshape((3,4)) 

# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

print(np.sort(A))    

# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])


# 矩阵的转置有两种表示方法：

print(np.transpose(A))    
print(A.T)

# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])


# 在Numpy中具有clip()函数
print(A)
# array([[14,13,12,11]
#        [10, 9, 8, 7]
#        [ 6, 5, 4, 3]])

print(np.clip(A,5,9))    
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])
# 这个函数的格式是clip(Array,Array_min,Array_max)，顾名思义，Array指的是将要被执行用的矩阵，
# 而后面的最小值最大值则用于让函数判断矩阵中元素是否有比最小值小的或者比最大值大的元素，
# 并将这些指定的元素转换为最小值或者最大值。
# 实际上每一个Numpy中大多数函数均具有很多变量可以操作，你可以指定行、列甚至某一范围中的元素。
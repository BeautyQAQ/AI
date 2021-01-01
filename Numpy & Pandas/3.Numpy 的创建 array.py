# 创建 array 有很多 形式

# array：创建数组
# dtype：指定数据类型
# zeros：创建数据全为0
# ones：创建数据全为1
# empty：创建数据接近0
# arrange：按指定范围创建数据
# linspace：创建线段
import numpy as np
a = np.array([2,23,4])  # list 1d
print(a)
# [2 23 4]

a = np.array([2,23,4],dtype=np.int64)
print(a.dtype)
# int 64

a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
# int32

a = np.array([2,23,4],dtype=np.float)
print(a.dtype)
# float64

a = np.array([2,23,4],dtype=np.float32)
print(a.dtype)
# float32

a = np.array([[2,23,4],[2,32,4]])  # 2d 矩阵 2行3列
print(a)

a = np.zeros((3,4)) # 数据全为0，3行4列
print(a)

a = np.ones((3,4),dtype = np.int)   # 数据为1，3行4列
print(a)

# 创建全空数组, 其实每个值都是接近于零的数:
a = np.empty((3,4)) # 数据为empty，3行4列
print(a)

a = np.arange(10,20,2) # 10-19 的数据，2步长
print(a)

a = np.arange(12).reshape((3,4))    # 3行4列，0到11
print(a)

# 用 linspace 创建线段型数据
a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
print(a)

a = np.linspace(1,10,20).reshape((5,4)) # 更改shape
print(a)
# Numpy array 合并
import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])

# 上下合并
print(np.vstack((A,B)))    # vertical stack
"""
[[1,1,1]
 [2,2,2]]
"""
# vertical stack本身属于一种上下合并，即对括号中的两个整体进行对应操作。此时我们对组合而成的矩阵进行属性探究：
C = np.vstack((A,B))      
print(A.shape,C.shape)

# (3,) (2,3)
# 利用shape函数可以让我们很容易地知道A和C的属性，
# 从打印出的结果来看，A仅仅是一个拥有3项元素的数组（数列），而合并后得到的C是一个2行3列的矩阵。


# 左右合并
D = np.hstack((A,B))       # horizontal stack

print(D)
# [1,1,1,2,2,2]

print(A.shape,D.shape)
# (3,) (6,)



# 转置
# 如果面对如同前文所述的A序列， 
# 转置操作便很有可能无法对其进行转置（因为A并不是矩阵的属性），此时就需要我们借助其他的函数操作进行转置：
print(A[np.newaxis,:])
# [[1 1 1]]

print(A[np.newaxis,:].shape)
# (1,3)

print(A[:,np.newaxis])
"""
[[1]
[1]
[1]]
"""

print(A[:,np.newaxis].shape)
# (3,1)
# newaxis方法就是增加一个维度



# 综合
import numpy as np
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
         
C = np.vstack((A,B))   # vertical stack
D = np.hstack((A,B))   # horizontal stack

print(D)
"""
[[1 2]
[1 2]
[1 2]]
"""

print(A.shape,D.shape)
# (3,1) (3,2)




# 当你的合并操作需要针对多个矩阵或序列时，借助concatenate函数可能会让你使用起来比前述的函数更加方便：
C = np.concatenate((A,B,B,A),axis=0)

print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A,B,B,A),axis=1)

print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""

# axis参数很好的控制了矩阵的纵向或是横向打印，相比较vstack和hstack函数显得更加方便。
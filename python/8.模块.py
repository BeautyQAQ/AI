# $ pip install numpy   # 这是 python2+ 版本的用法
# $ pip3 install numpy   # 这是 python3+ 版本的用法

# $ pip install -U numpy   # 这是 python2+ 版本的用法
# $ pip3 install -U numpy   # 这是 python3+ 版本的用法

# import的各种方法
import time
print(time.localtime())  #这样就可以print 当地时间了

import time as t
print(t.localtime()) # 需要加t.前缀来引出功能

# 只import自己想要的功能.
from time import time, localtime
print(localtime())
print(time())

# 输入模块的所有功能
from time import *
print(localtime())

import balance


# 模块存储路径说明 
# 在Mac系统中，下载的python模块会被存储到外部路径site-packages，
# 同样，我们自己建的模块也可以放到这个路径，最后不会影响到自建模块的调用。
# Pandas 导入导出

# 要点
# pandas可以读取与存取的资料格式有很多种，像csv、excel、json、html与pickle等…， 详细请看官方说明文件

# 读取csv
import pandas as pd #加载模块

#读取csv
data = pd.read_csv('student.csv')

#打印出data
print(data)


# 将资料存取成pickle 
data.to_pickle('student.pickle')
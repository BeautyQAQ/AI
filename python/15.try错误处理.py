# 错误处理
try:
    file=open('eeee.txt','r')  #会报错的代码
except Exception as e:  # 将报错存储在 e 中
    print(e)

# 处理错误：会使用到循环语句。首先报错：没有这样的文件No such file or directory. 
# 然后决定是否输入y, 输入y以后，系统就会新建一个文件（要用写入的类型），再次运行后，文件中就会写入ssss
try:
    file=open('eeee.txt','r+')
except Exception as e:
    print(e)
    response = input('do you want to create a new file:')
    if response=='y':
        file=open('eeee.txt','w')
    else:
        pass
else:
    file.write('ssss')
    file.close()
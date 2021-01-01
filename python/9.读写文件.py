# 换行命令
# 定义 text 为字符串, 并查看使用 \n 和不适用 \n 的区别:
text='This is my first test. This is the second line. This the third '
print(text)  # 无换行命令

text='This is my first test.\nThis is the second line.\nThis the third line'
print(text)   # 输入换行命令\n，要注意斜杆的方向。注意换行的格式和c++一样

# open 读文件方式
my_file=open('my file.txt','w')   #用法: open('文件名','形式'), 其中形式有'w':write;'r':read.
my_file.write(text)               #该语句会写入先前定义好的 text
my_file.close()                   #关闭文件

# tab 对齐 
# 使用 \t 能够达到 tab 对齐的效果:
text='\tThis is my first test.\n\tThis is the second line.\n\tThis is the third line'
print(text)  #延伸 使用 \t 对齐


# 给文件增加内容
append_text='\nThis is appended file.'  # 为这行文字提前空行 "\n"
my_file=open('my file.txt','a')   # 'a'=append 以增加内容的形式打开
my_file.write(append_text)
my_file.close()

# 读取文件内容 file.read()
file=open('my file.txt','r') 
content=file.read()  
print(content)

# 按行读取 file.readline()
file= open('my file.txt','r') 
content=file.readline()  # 读取第一行 readline()读取第几行跟使用次数相关
print(content)
# 读取所有行 file.readlines()
file= open('my file.txt','r') 
content=file.readlines() # python_list 形式
print(content)
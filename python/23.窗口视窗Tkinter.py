# 什么是 Tkinter
# Tkinter 是使用 python 进行窗口视窗设计的模块.

# Label & Button 标签和按钮
# 窗口主体框架
# import tkinter as tk

# window = tk.Tk()
# window.title('my window')
# window.geometry('200x100')

# 这里是窗口的内容
# l = tk.Label(window, 
#     text='OMG! this is TK!',    # 标签的文字
#     bg='green',     # 背景颜色
#     font=('Arial', 12),     # 字体和字体大小
#     width=15, height=2  # 标签长宽
#     )
# l.pack()    # 固定窗口位置

# var = tk.StringVar()    # 这时文字变量储存器
# l = tk.Label(window, 
#     textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
#     bg='green', font=('Arial', 12), width=15, height=2)
# l.pack() 

# on_hit = False  # 默认初始状态为 False
# def hit_me():
#     global on_hit
#     if on_hit == False:     # 从 False 状态变成 True 状态
#         on_hit = True
#         var.set('you hit me')   # 设置标签的文字为 'you hit me'
#     else:       # 从 True 状态变成 False 状态
#         on_hit = False
#         var.set('') # 设置 文字为空

# # 按钮
# b = tk.Button(window, 
#     text='hit me',      # 显示在按钮上的文字
#     width=15, height=2, 
#     command=hit_me)     # 点击按钮式执行的命令
# b.pack()    # 按钮位置

# window.mainloop()



# Entry & Text 输入, 文本框
# import tkinter as tk

# window = tk.Tk()
# window.title('my window')

# ##窗口尺寸
# window.geometry('200x200')

# # 定义触发事件时的函数
# def insert_point():
#     var = e.get()
#     t.insert('insert',var)

# def insert_end():
#     var = e.get()
#     t.insert('end',var)

# b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
# b1.pack()

# b2 = tk.Button(window,text="insert end",command=insert_end)
# b2.pack()
# # 输入框entry
# e = tk.Entry(window,show='*')
# e.pack()
# # 文本框
# t = tk.Text(window,height=2)
# t.pack()
# ##显示出来
# window.mainloop()


# Listbox 列表部件
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# var1 = tk.StringVar()    #创建变量
# l =tk.Label(window,bg='yellow',width=4,textvariable=var1)
# l.pack()

# def print_selection():
#     value = lb.get(lb.curselection())   #获取当前选中的文本
#     var1.set(value)     #为label设置值

# b1 = tk.Button(window, text='print selection', width=15,
#               height=2, command=print_selection)
# b1.pack()

# var2 = tk.StringVar()
# var2.set((11,22,33,44)) #为变量设置值

# #创建Listbox

# lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

# #创建一个list并将值循环添加到Listbox控件中
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end', item)  #从最后一个位置开始加入值
# lb.insert(1, 'first')       #在第一个位置加入'first'字符
# lb.insert(2, 'second')      #在第二个位置加入'second'字符
# lb.delete(2)                #删除第二个位置的字符
# lb.pack()

# window.mainloop()


# Radiobutton 选择按钮
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# var = tk.StringVar()
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()

# def print_selection():
#     l.config(text='you have selected ' + var.get())

# r1 = tk.Radiobutton(window, text='Option A',
#                     variable=var, value='A',
#                     command=print_selection)
# r1.pack()
# window.mainloop()



# Scale 尺度
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# def print_selection(v):
#     l.config(text='you have selected ' + v)

# s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
#              length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
# s.pack()

# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()

# window.mainloop()




# Checkbutton 勾选项
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# l = tk.Label(window, bg='yellow', width=20, text='empty')

# var2 = tk.StringVar()

# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
#         l.config(text='I love only Python ')
#     elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
#         l.config(text='I love only C++')
#     elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
#         l.config(text='I do not love either')
#     else:
#         l.config(text='I love both')             #如果两个选项都选中

# var1 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
#                     command=print_selection)
# c1.pack()
# window.mainloop()



# Canvas 画布
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# canvas.pack()
# image_file = tk.PhotoImage(file='ins.gif')
# image = canvas.create_image(10, 10, anchor='nw', image=image_file)

# x0, y0, x1, y1= 50, 50, 80, 80
# line = canvas.create_line(x0, y0, x1, y1)

# oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
# arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形

# def moveit():
#     canvas.move(rect, 0, 2)
# window.mainloop()



# Menubar 菜单
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# ##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
# menubar = tk.Menu(window)

# ##定义一个空菜单单元
# filemenu = tk.Menu(menubar, tearoff=0)

# ##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
# menubar.add_cascade(label='File', menu=filemenu)
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# counter = 0
# def do_job():
#     global counter
#     l.config(text='do '+ str(counter))
#     counter+=1
# ##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
# ##如果点击这些单元, 就会触发`do_job`的功能
# filemenu.add_command(label='New', command=do_job)
# filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
# filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单

# filemenu.add_separator()##这里就是一条分割线

# ##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
# filemenu.add_command(label='Exit', command=window.quit)

# submenu = tk.Menu(filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
# filemenu.add_cascade(label='Import', menu=submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
# submenu.add_command(label="Submenu1", command=do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`

# window.mainloop()


# Frame 框架
# Frame 是一个在 Windows 上分离小区域的部件, 它能将 Windows 分成不同的区,然后存放不同的其他部件. 
# 同时一个 Frame 上也能再分成两个 Frame, Frame 可以认为是一种容器.
###定义一个`label`显示`on the window`
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# tk.Label(window, text='on the window').pack()

# ###在`window`上创建一个`frame`
# frm = tk.Frame(window)
# frm.pack()

# ###在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`

# frm_l = tk.Frame(frm)
# frm_r = tk.Frame(frm)

# ###这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
# frm_l.pack(side='left')
# frm_r.pack(side='right')

# ###这里的三个label就是在我们创建的frame上定义的label部件，还是以容器理解，就是容器上贴了标签，来指明这个是什么，解释这个容器。
# tk.Label(frm_l, text='on the frm_l1').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l1`
# tk.Label(frm_l, text='on the frm_l2').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l2`
# tk.Label(frm_r, text='on the frm_r1').pack()##这个`label`长在`frm_r`上，显示为`on the frm_r1`
# window.mainloop()


# messagebox 弹窗
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# def hit_me():
#    tk.messagebox.showinfo(title='Hi', message='hahahaha')

# tk.Button(window, text='hit me', command=hit_me).pack()

# tk.messagebox.showinfo(title='',message='')#提示信息对话窗
# tk.messagebox.showwarning()#提出警告对话窗
# tk.messagebox.showerror()#提出错误对话窗
# tk.messagebox.askquestion()#询问选择对话窗

# def hit_me():
#     print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))
#     print(tk.messagebox.askquestion())#返回yes和no
#     print(tk.messagebox.askokcancel())#返回true和false
#     print(tk.messagebox.askyesno())#返回true和false
#     print(tk.messagebox.askretrycancel())#返回true和false

# window.mainloop()


# pack grid place 放置位置
# import tkinter as tk
# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# tk.Label(window, text='1').pack(side='top')#上
# tk.Label(window, text='1').pack(side='bottom')#下
# tk.Label(window, text='1').pack(side='left')#左
# tk.Label(window, text='1').pack(side='right')#右

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

# window.mainloop()



# place 
# 就是给精确的坐标来定位，如此处给的（20,10），
# 就是将这个部件放在坐标为（x，y）的这个位置 后面的参数anchor=nw就是前面所讲的锚定点是西北角。
import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()
# 多线程
# 多线程是加速程序计算的有效方式，Python的多线程模块threading上手快速简单，从这节开始我们就教大家如何使用它。

# 添加线程
# import threading

# # 获取已激活的线程数
# print(threading.active_count())
# # 查看所有线程信息
# print(threading.enumerate())


# # threading.Thread()接收参数target代表这个线程要完成的任务，需自行定义
# def thread_job():
#     print('This is a thread of %s' % threading.current_thread())

# def main():
#     thread = threading.Thread(target=thread_job,)   # 定义线程 
#     thread.start()  # 让线程开始工作
    
# if __name__ == '__main__':
#     main()


# # join
# # 不加join的结果
# import threading
# import time

# def thread_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1) # 任务间隔0.1s
#     print("T1 finish\n")

# added_thread = threading.Thread(target=thread_job, name='T1')
# added_thread.start()
# print("all done\n")


# # 加入join的结果
# import threading
# import time

# def T1_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print("T1 finish\n")

# def T2_job():
#     print("T2 start\n")
#     print("T2 finish\n")

# thread_1 = threading.Thread(target=T1_job, name='T1')
# thread_2 = threading.Thread(target=T2_job, name='T2')
# # 为了规避不必要的麻烦，推荐如下这种1221的V型排布
# thread_1.start() # start T1
# thread_2.start() # start T2
# thread_2.join() # join for T2
# thread_1.join() # join for T1
# print("all done\n")



# 储存进程结果 Queue
# 将数据列表中的数据传入，使用四个线程处理，将结果保存在Queue中，线程执行完后，从Queue中获取存储的结果
# import threading
# import time
# from queue import Queue
# # 函数的参数是一个列表l和一个队列q，函数的功能是，对列表的每个元素进行平方计算，将结果保存在队列中
# def job(l,q):
#     for i in range (len(l)):
#         l[i] = l[i]**2
#     q.put(l)   #多线程调用的函数不能用return返回值

# # 在多线程函数中定义一个Queue，用来保存返回值，代替return，定义一个多线程列表，初始化一个多维数据列表，用来处理：
# def multithreading():
#     q =Queue()    #q中存放返回值，代替return的返回值
#     threads = []
#     data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]

#     # 在多线程函数中定义四个线程，启动线程，将每个线程添加到多线程的列表中
#     for i in range(4):   #定义四个线程
#         t = threading.Thread(target=job,args=(data[i],q)) #Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
#         t.start()#开始线程
#         threads.append(t) #把每个线程append到线程列表中

#     # 分别join四个线程到主线程
#     for thread in threads:
#         thread.join()

#     # 定义一个空的列表results，将四个线运行后保存在队列中的结果返回给空列表results
#     results = []
#     for _ in range(4):
#         results.append(q.get())  #q.get()按顺序从q中拿出一个值
#     print(results)

# if __name__=='__main__':
#     multithreading()


# GIL 不一定有效率
# python 的多线程 threading 有时候并不是特别理想. 最主要的原因是就是, Python 的设计上, 有一个必要的环节,
# 就是 Global Interpreter Lock (GIL). 这个东西让 Python 还是一次性只能处理一个东西.

# GIL：尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。 
# 实际上，解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。 
# GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势 （比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。
# 在讨论普通的GIL之前，有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。 
# 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。
# 实际上，你完全可以放心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。


# 测试 GIL
# 创建一个 job, 分别用 threading 和 一般的方式执行这段程序. 并且创建一个 list 来存放我们要处理的数据. 
# 在 Normal 的时候, 我们这个 list 扩展4倍, 在 threading 的时候, 我们建立4个线程, 并对运行时间进行对比.
# import threading
# from queue import Queue
# import copy
# import time

# def job(l, q):
#     res = sum(l)
#     q.put(res)

# def multithreading(l):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
#         t.start()
#         threads.append(t)
#     [t.join() for t in threads]
#     total = 0
#     for _ in range(4):
#         total += q.get()
#     print(total)

# def normal(l):
#     total = sum(l)
#     print(total)

# if __name__ == '__main__':
#     l = list(range(1000000))
#     s_t = time.time()
#     normal(l*4)
#     print('normal: ',time.time()-s_t)
#     s_t = time.time()
#     multithreading(l)
#     print('multithreading: ', time.time()-s_t)
# 我们的运算结果没错, 所以程序 threading 和 Normal 运行了一样多次的运算.
# 但是我们发现 threading 却没有快多少, 按理来说, 我们预期会要快3-4倍, 因为有建立4个线程, 但是并没有. 这就是其中的 GIL 在作怪.



# 线程锁Lock
# 不使用 Lock 的情况
# 全局变量A的值每次加1，循环10次，并打印
import threading
# def job1():
#     global A
#     for i in range(10):
#         A+=1
#         print('job1',A)
# # 函数二：全局变量A的值每次加10，循环10次，并打印
# def job2():
#     global A
#     for i in range(10):
#         A+=10
#         print('job2',A)

# # 主函数：定义两个线程，分别执行函数一和函数二
# if __name__== '__main__':
#     A=0
#     t1=threading.Thread(target=job1)
#     t2=threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# 使用 Lock 的情况
# 函数一和函数二加锁
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()
# 主函数中定义一个Lock
if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
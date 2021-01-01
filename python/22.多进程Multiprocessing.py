# 什么是 Multiprocessing
# 多进程 Multiprocessing 和多线程 threading 类似, 他们都是在 python 中用来并行运算的. 
# 不过既然有了 threading, 为什么 Python 还要出一个 multiprocessing 呢? 
# 原因很简单, 就是用来弥补 threading 的一些劣势, 比如在 threading 教程中提到的GIL.
# 使用 multiprocessing 也非常简单, 如果对 threading 有一定了解的朋友, 你们的享受时间就到了. 
# 因为 python 把 multiprocessing 和 threading 的使用方法做的几乎差不多. 
# 这样我们就更容易上手. 也更容易发挥你电脑多核系统的威力了


# 添加进程 Process
# 导入线程进程标准模块
# import multiprocessing as mp
# import threading as td
# # 定义一个被线程和进程调用的函数
# def job(a,d):
#     print('aaaaa')
# # 创建线程和进程
# t1 = td.Thread(target=job,args=(1,2))
# p1 = mp.Process(target=job,args=(1,2))
# # 注意：Thread和Process的首字母都要大写，被调用的函数没有括号，被调用的函数的参数放在args(...)中
# # 线程和进程的使用方法相似
# # t1.start()
# # p1.start()
# # t1.join()
# # p1.join()
# if __name__=='__main__':
#     p1 = mp.Process(target=job,args=(1,2))
#     p1.start()
#     p1.join()


# 存储进程输出 Queue
# 多线程/多进程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果

# 把结果放在 Queue 里
#该函数没有返回值！！！
# import multiprocessing as mp
# def job(q):
#     res=0
#     for i in range(1000):
#         res+=i+i**2+i**3
#     q.put(res)    #queue

# if __name__=='__main__':
#     q = mp.Queue()
#     # args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
#     p1 = mp.Process(target=job,args=(q,))
#     p2 = mp.Process(target=job,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1+res2)



# 效率对比 threading & multiprocessing
# 创建多进程 multiprocessing
# import multiprocessing as mp

# def job(q):
#     res = 0
#     for i in range(1000000):
#         res += i + i**2 + i**3
#     q.put(res) # queue

# def multicore():
#     q = mp.Queue()
#     p1 = mp.Process(target=job, args=(q,))
#     p2 = mp.Process(target=job, args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print('multicore:',res1 + res2)


# # 创建多线程 multithread ¶
# import threading as td

# def multithread():
#     q = mp.Queue() # thread可放入process同样的queue中
#     t1 = td.Thread(target=job, args=(q,))
#     t2 = td.Thread(target=job, args=(q,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print('multithread:', res1 + res2)


# # 创建普通函数 
# def normal():
#     res = 0
#     for _ in range(2):
#         for i in range(1000000):
#             res += i + i**2 + i**3
#     print('normal:', res)


# # 运行时间
# import time

# if __name__ == '__main__':
#     st = time.time()
#     normal()
#     st1 = time.time()
#     print('normal time:', st1 - st)
#     multithread()
#     st2 = time.time()
#     print('multithread time:', st2 - st1)
#     multicore()
#     print('multicore time:', time.time() - st2)
# 普通/多线程/多进程的运行时间分别是1.13，1.3和0.64秒。 我们发现多核/多进程最快，说明在同时间运行了多个任务。 
# 而多线程的运行时间居然比什么都不做的程序还要慢一点，说明多线程还是有一定的短板的。


# 进程池 Pool
# import multiprocessing as mp

# def job(x):
#     return x*x
# # 然后我们定义一个Pool
# # pool = mp.Pool()
# # 有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。
# # Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。
# def multicore():
#     pool = mp.Pool()
#     res = pool.map(job, range(10))
#     print(res)
    
# if __name__ == '__main__':
#     multicore()


# # Pool默认大小是CPU的核数，我们也可以通过在Pool中传入processes参数即可自定义需要的核数量
# def multicore():
#     pool = mp.Pool(processes=3) # 定义CPU核数量为3
#     res = pool.map(job, range(10))
#     print(res)



# # apply_async()
# # Pool除了map()外，还有可以返回结果的方式，那就是apply_async().
# # apply_async()中只能传递一个值，它只会放入一个核进行运算，
# # 但是传入值时要注意是可迭代的，所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
# def multicore():
#     pool = mp.Pool() 
#     res = pool.map(job, range(10))
#     print(res)
#     res = pool.apply_async(job, (2,))
#     # 用get获得结果
#     print(res.get())
#     # 迭代器，i=0时apply一次，i=1时apply一次等等
#     multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
#     # 从迭代器中取出
#     print([res.get() for res in multi_res])



# 共享内存 
# 只有用共享内存才能让CPU之间有交流。

# Shared Value
# import multiprocessing as mp
# 其中d和i参数用来设置数据类型的，d表示一个双精浮点类型，i表示一个带符号的整型
# value1 = mp.Value('i', 0) 
# value2 = mp.Value('d', 3.14)

# Shared Array
# 在Python的mutiprocessing中，有还有一个Array类，可以和共享内存交互，来实现在进程之间共享数据
# 这里的Array和numpy中的不同，它只能是一维的，不能是多维的。同样和Value 一样，需要定义数据形式，否则会报错
# array = mp.Array('i', [1, 2, 3, 4])
# 参考数据形式  各参数代表的数据类型
# | Type code | C Type             | Python Type       | Minimum size in bytes |
# | --------- | ------------------ | ----------------- | --------------------- |
# | `'b'`     | signed char        | int               | 1                     |
# | `'B'`     | unsigned char      | int               | 1                     |
# | `'u'`     | Py_UNICODE         | Unicode character | 2                     |
# | `'h'`     | signed short       | int               | 2                     |
# | `'H'`     | unsigned short     | int               | 2                     |
# | `'i'`     | signed int         | int               | 2                     |
# | `'I'`     | unsigned int       | int               | 2                     |
# | `'l'`     | signed long        | int               | 4                     |
# | `'L'`     | unsigned long      | int               | 4                     |
# | `'q'`     | signed long long   | int               | 8                     |
# | `'Q'`     | unsigned long long | int               | 8                     |
# | `'f'`     | float              | float             | 4                     |
# | `'d'`     | double             | float             | 8                     | 


# 进程锁 Lock

# 不加进程锁
import multiprocessing as mp
import time

# def job(v, num):
#     for _ in range(5):
#         time.sleep(0.1) # 暂停0.1秒，让输出效果更明显
#         v.value += num # v.value获取共享变量值
#         print(v.value, end="")
        
# def multicore():
#     v = mp.Value('i', 0) # 定义共享变量
#     p1 = mp.Process(target=job, args=(v,1))
#     p2 = mp.Process(target=job, args=(v,3)) # 设定不同的number看如何抢夺内存
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
    
# if __name__ == '__main__':
#     multicore()

# 加进程锁
def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放

def multicore():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()
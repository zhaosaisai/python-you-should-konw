### 进程间通信

Process的不同进程之间是可以相互通信的。在python中，我们可以使用`multiprocessing.Queue`来实现进程之间的通信。Queue可以看成是一个消息队列的程序。

一个小的🌰：

```python
# coding:utf-8
from multiprocessing import Queue

q = Queue(3) # 初始化一个Queue对象，这个对象最多可以put三条信息
# 查看队列是不是空的
print q.empty() # True
q.put('消息1')
q.put('消息2')
# 判断队列中的信息是否达到了最大的容量
print q.full() # False
q.put('消息3') 
print q.full() # True

# 判断队列中存储的消息的数量
print q.qsize() # 3
# 取出一个数据
print q.get() # 消息1
print q.qsize() # 2

# 如果消息的队列已经满了，当我们再次向其中put内容的时候，会报错
```
注意：q.put()和q.get()都是堵塞进程的方法，也就是说，当队列中的数据达到队列所允许的最大值的时候，继续调用q.put()方法向队列中添加数据的时候，程序会等待，知道队列接收这个添加的数据。而当队列是empty()的时候，如果继续调用q.get()，程序仍然会等待，直到队列中有元素可以取出来的时候。与之相对的有两个方法，分别是`q.put_nowait()`和`q.get_nowait()`，当程序为full或者empty状态的时候，继续调用，会抛出异常。

> 进程间通信的案例

下面是一个进程间通信的一个案例：

```python
from multiprocessing import Process, Queue
import os
import time
import random

# 写数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C']:
        q.put(value)
        time.sleep(random.random())
        
# 读数据进程代码
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print 'get %s from queue' % value
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 主进程用于创建队列
    q = Queue()
    # 创建一个写进程
    pw = Process(target=write, args=(q,))
    # 创建一个读进程
    pr = Process(target=read, args=(q,))
    
    # 启动写进程
    pw.start()
    # 等待写结束
    pw.join()
    
    # 启动读进程
    pr.start()
    # 等待读进程结束
    pr.join()
    
    print '数据读写结束'
```

> 进程池之间的进程通信

进程池创建的进程之间是不能够直接使用Queue()方法进行通信的。我们必须借助于`multiprocessing.Manager().Queue()`方法进行通信。

```python
from multiprocessing import Manager, Pool
import os
import time
import random

def reader(q):
    print "reader启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid())
    for i in range(q.qsize()):
        print 'ge data from queue:\t%s' % q.get(True)

def writer(q):
    print "reader启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid())
    for v in ['A', 'B', 'C']:
        q.put(v)
        
if __name__ == '__main__':
    print '(%s) start' % os.getpid()
    q = Manager().Queue() # 创建一个队列
    pool = Pool() # 创建一个进程池
    
    # 使用阻塞的方式创建进程，其主要作用就是我们不需要在reader中再次进行死循环了，可以保证在wriiter完全执行成功后再执行reader
    pool.apply(writer, (q,))
    pool.apply(reader, (q,))
    
    pool.close()
    pool.join()
    
    print '(%s) end' % os.getpid()
```
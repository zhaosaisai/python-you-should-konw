### pdb调试
pdb是一个基于命令行的python程序调试工具。

> 执行时调试

```bash
python -m pdb some.py
```
以pdb模块运行我的程序。

比如下面的这个文件check.py：

```python
def getAverage(a, b):
    result = a + b
    print "result=%d" % result
    return result

a = 100
b = 200
c = a + b

ret = getAverage(a, b)
```
以pdb的模式运行下面的文件。

```bash
python -m pdb check.py
```
会显示如下的界面，就表示已经进入了pdb的调试模式了。

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjuhm4vu7aj30hs04uq3d.jpg)

进入pdb调试的时候，根据不同的输入可以获取不同的功能。下面是一些常见的功能。

* l：查看文件的源代码

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjuhr59eisj309n08iaap.jpg)

其中，箭头所指的那一行，就是我们程序运行至的那一行。

* n：向下执行一步

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjuhtnk41kj30ee08i3z8.jpg)

* c：continue，继续执行代码。一次行执行后续的所有代码。

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjum1x9a43j30d9038aaa.jpg)

* b：加断点，一般格式是－－b 行号。如`b 8`表示给第8行加一个断点，则程序运行到第8行就会停止。

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjum8giglrj30co01lt8p.jpg)

其中`b`命令可以查看所有的断点。

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjumc2p4f6j30e3022wek.jpg)

* clear：`clear bid`清除指定的断点，bid就是通过b命令查看的所有的断点之前的序号。如`clear 1`。

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjumi0yrlsj30fh03xweu.jpg)

* s：进入函数调用
* p：打印一个变量的值
* a：打印一个参数的所有的形参数据

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjumrzgzd6j30np0pg0wj.jpg)

* r：快速执行到某个函数的最后一行

* q：退出调试程序

> 交互调试

进入到python解释器后，引入pgb模块。

```python
import pdb
pdb.run('testfun(args)') # 这就会打开pdb模式,进入之后要使用s命令进入到函数调用。
```
![](http://ww1.sinaimg.cn/large/006FmM8yly1fjunfr8a87j30si0o0wh5.jpg)

> 程序埋点

在程序中导入pdb模块，然后使用`pdb.set_trace()`方法设置埋点。当程序运行到这行代码的时候就会进入到调试模式。

```python
...
import pdb
pdb.set_trace()
...
```

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjunljjaeqj315o0eatah.jpg)

![](http://ww1.sinaimg.cn/large/006FmM8yly1fjunlyua8yj313604idgj.jpg)
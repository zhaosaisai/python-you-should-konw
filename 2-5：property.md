### property
>为私有属性添加getter和setter

```python
class Test(object):
    def __init__(self):
        self.__num = 0
    
    # num属性的getter
    def getNum(self):
        return self.__num
    
    # 设置num的属性
    def setNum(self, num):
        self.__num = num
```

> 使用property来描述setter和getter


```python
class Test(object):
    def __init__(self):
        self.__num = 0
    
    # num属性的getter
    def getNum(self):
        return self.__num
    
    # 设置num的属性
    def setNum(self, num):
        self.__num = num
    
    # 这个就是property的使用property(getter, setter)
    num = property(getNum, setNum)

# 借助于property我们可以像下面这样使用num
# 获取num
test.num # 0
# 设置num
test.num = 20
test.num # 20
```
property的作用相当于把setter和getter进行了封装，方便我们操作属性。

我们也可以使用装饰器来使用property。

```python
class Test(object):
    def __init__(self):
        self.__num = 0
        
    # getter
    @property
    def num(self):
        return self.__num
        
    #setter
    @num.setter
    def num(self, num):
        self.__num = num

# 获取num
test.num # 0
# 设置num
test.num = 20
test.num # 20
```
上面的class中的setter好人getter的函数名称相同。
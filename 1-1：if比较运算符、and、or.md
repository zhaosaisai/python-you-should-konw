##1-1：if比较运算符、and、or、not

> if语句的总体格式

```python
if 条件1:
    statement1
elif 条件2:
    statement2
else:
    statement3
```


1.比较运算符

```python
age = 10
if age >= 18: 
    print('大于等于')

if age <= 18:
    print('小于等于')
    
if age == 18:
    print('等于')

if age != 18:
    print('不等于')
```
2.逻辑运算符

```python
you = input('你去吗') # 去或者不去
your_wife = input('你老婆去吗') #去或者不去

# 或运算符
if you == '去' or your_wife == '去':
    print('it is ok')

# 与运算符
if you == '去' and your_wife == '去':
    print('very good')
```

**DEMO01**
```python
ok = input('Are you ok?')
love = input('Do you lobe me?')

if ok === 'ok' and love = 'yes':
    print('wonderful')
```
3.not运算符

```python
a = 30
if a > 0 and a <= 50:
    print('0<a<=50')

if not (a > 0 and a <= 50):
    print('a不在0-50之间')
```

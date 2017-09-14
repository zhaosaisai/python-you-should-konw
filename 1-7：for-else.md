### for-else

```python
num = [1, 2, 3, 4, 5]
for i in num:
    print i
else:
    print('over')

# 遍历结果如下
# 1
# 2
# 3
# 4
# 5
# over

for i in num:
    print i
    if i > 2:
        break
else:
    print 'over'

# 结果是
# 1
# 2
# 3
```
说明for循环执行过程中，如果执行了break语句，则else语句也是不会执行的。否则，else一定会执行的。
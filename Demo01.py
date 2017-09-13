#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

print('='*50)
print('1. 添加一个新的名字')
print('2. 删除一个名字')
print('3. 修改一个名字')
print('4. 查询一个名字')
print('5. 列出所有的名字')
print('='*50)


# 存储添加的名字 
names = []

while True:
     # 获取输入
    num = int(raw_input('请输入功能序号：'))
    # 对应的功能
    if num == 1:
        new_name = raw_input('请输入你的新名字：')
        names.append(new_name)
        print names
    elif num == 2:
        delete_name = raw_input('请输入你要删除的名字：')
        if delete_name in names:
            print '你要删除的是：%s' % delete_name
            yn = raw_input('你确认删除 %s吗？(y/n)' % delete_name)
            if yn.lower() == 'y':
                names.remove(delete_name)
                print '删除成功'
        else:
            print '没有这个人，请重新输入。'
    elif num == 3:
        replace_name = raw_input('请输入旧名称：')
        if replace_name in names:
            new_name = raw_input('请输入新名称：')
            old_index = names.index(replace_name)
            names[old_index] = new_name
            print '修改成功'
        else:
            print '你输入的名字，不再系统中，请重新输入。'
    elif num == 4:
        find_name = raw_input('请输入你查找的名字'：)
        if find_name in names:
            print '找到了这个人'
        else:
            print '没有这个人'
    elif num == 5:
        print names
    else:
        exit('你输入的序号有误，请输入1，2，3，4之一')

#!/usr/bin/env python
#-*- coding:utf-8 -*-
from multiprocessing import Pool, Manager
import os
import time

def copy_file_task(name, old_folder_name, new_folder_name, queue):
     fr = open(old_folder_name + '/' + name)
     fw = open(new_folder_name + '/' + name, 'w+')

     fw.write(fr.read())

     fr.close()
     fw.close()
     
     queue.put(name)
     time.sleep(1)
def main():	
     # 获取需要copy的文件夹的名字
     old_folder_name = raw_input('请输入你要复制的文件夹的名字：')
     # 设置新的文件夹的名字
     new_folder_name = old_folder_name + '.bak'
     # 创建新的文件夹
     os.mkdir(new_folder_name)
     # 获取旧文件夹下面所有的文件
     file_names = os.listdir(old_folder_name)
     
     # 使用多进程的方式copy文件
     pool = Pool(5)
     q = Manager().Queue()
     for name in file_names:         
        pool.apply_async(copy_file_task, args=(name,old_folder_name, new_folder_name, q))
     
     num = 0
     all_num = len(file_names)
     while True:
         q.get()
         num += 1
         print '进度%.2f' % (num * 100 / all_num)
         if num == all_num:
             break

     pool.close()
     pool.join()
if __name__ == '__main__':
	main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 上午10:01
# @Author  : Ryan Xu
# @Site    : 
# @File    : with_file.py
# @Software: PyCharm


from datetime import datetime


#写文件 w , wb

# with open("/Users/ryanxu/Documents/py_test.txt", "w", encoding='utf-8') as f:
#     f.write("Hello, 今天是 ")
#     f.write(datetime.now().strftime("%Y-%m-%d"))


with open("/Users/ryanxu/Documents/py_test.txt", "r", encoding='utf-8') as f:
    info = f.read()
    print(info)

with open("/Users/ryanxu/Documents/py_test.txt", "rb") as f:
    info = f.read()
    print("open as binary for read...")
    print(info)
    print(str(info.decode(encoding="utf-8")))





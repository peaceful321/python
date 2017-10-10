#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 下午6:35
# @Author  : Ryan Xu
# @Site    : 
# @File    : io_sync.py
# @Software: PyCharm
# desc     : python 同步io

#读文件

f = open("/Users/ryanxu/Documents/admin/LinuxCMD/test.txt", 'r')

#read() 方法， 一次读取文件的全部内容， python 把内容读取到内存， 用一个str 对象表示
try:
    print(f.read())
finally:
    if f:
        f.close

#加 try 比较麻烦， 建议使用with, 不必调用 close() 方法
with open("/Users/ryanxu/Documents/admin/LinuxCMD/test.txt", 'r') as f:
    print(f.read())


#调用 read() 方法会一次性读取文件的全部内容， 如果文件有10G， 那么内存就爆了， 所以 可以反复调用 read(size) 方法， 每次最多读取size个字节的内容；
#另外，readline() 方法可以每次读取一行内容， 调用 readlines() 一次读取所有内容，并按行返回list。 因此， 要根据需要决定怎么调用
#如果文件较小， 可以read() 方法一次性读取 最方便； 如果不能确定文件大小， 反复调用read(size) 比较保险； 如果是配置文件， 调用readlines() 最方便；
f = open("/Users/ryanxu/Documents/admin/LinuxCMD/test.txt", 'r')
for line in f.readlines():
    print(line.strip()) #strip() 把末尾的 '\n' 删掉


#二进制文件
#上面所述都是读取文本文件， 并且是utf-8 编码的文本文件。 要读取二进制文件， 如：image，音视频 等，则用 'rb' 模式打开文件即可
with open('/Users/ryanxu/Downloads/imgs/a0.jpg', 'rb') as f_img:
    print(f_img.read())

#字符编码
#要读取非 utf-8 的文本文件， 需要给 open() 函数传入encoding 参数
with open('/Users/ryanxu/Documents/admin/LinuxCMD/test.txt', 'r', encoding='gbk') as file:
    print(file.read())

#遇到有些编码不规范的文件， 可能会遇到 UnicodeDecodeError， 因为文件中可能夹杂一些非法编码的字符。 此时 open() 函数可以接收一个 errors 参数，表示遇到编码错误后如何处理。
with open('/Users/ryanxu/Documents/admin/LinuxCMD/test.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())


#####################################################################################################################################################

#写文件
#写文件和读文件 基本是一样的， 唯一的区别是调用open()函数时， 传入的标识符 是 'w' or 'wb' 分别表示 写文本文件或写二进制文件

with open("/Users/ryanxu/Documents/admin/LinuxCMD/test_10_10.txt", 'w') as f_w:
    f_w.write("Hello world")


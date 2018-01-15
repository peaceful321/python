#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 上午10:31
# @Author  : Ryan Xu
# @Site    : 
# @File    : pickling.py
# @Software: PyCharm

#序列化， 把变量从内存中编程可存储或传输的过程称之为序列化； java 中叫做 serialization
#序列化后，则可以把序列化后的内容写入磁盘， 或者通过网络传输到别的机器上
#反序列化， 则是把变量内容从序列化的对象重新读到内存里称之为 反序列化，即：unpickling
#python 提供pickle 模块来实现序列化

import pickle

#创建一个字典 d
d = dict(name="Ryan", age = 25, gender = "man")

#pickle.dumps（） 方法可以把任意对象序列化为一个bytes， 然后，就可以把这个 bytes 写入文件；或者用另一个方法pickle.dump() 直接把对象序列化后写入一个 file-like-Object

buf = pickle.dumps(d)
print(buf)

#序列化， 从内存中，写入到一个磁盘文件中
with open("/Users/ryanxu/Downloads/d.txt", "wb") as f:
    pickle.dump(d, f)


#反序列化， 从file-like-Object 中读取到内存
with open('/Users/ryanxu/Downloads/d.txt', 'rb') as file:
    dd = pickle.load(file)

print("dd = " + str(dd))



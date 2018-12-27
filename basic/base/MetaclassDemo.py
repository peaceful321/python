#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午6:42
# @Author  : Ryan Xu
# @Site    : 
# @File    : MetaclassDemo.py
# @Software: PyCharm


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)



class MyList(list, metaclass = ListMetaclass):
    pass



mList = MyList()
mList.add(1)

print("mList : ", mList)



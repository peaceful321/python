#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午11:33
# @Author  : Ryan Xu
# @File    : use_custom_made.py
# @Software: PyCharm


class Spical(object):
    """
    定制化 类 
    """

    def __init__(self):
        self.__name = "定制化类";


    def __str__(self):
        return "Spical object (name : %s)" %self.__name

    __repr__ = __str__


    def __getattr__(self, attr):
        if attr == "name":
            return self.__name
        if attr == "age":
            raise AttributeError("\'Spical\' has no attribute \'%s\'" %attr)


#测试
s = Spical()
print(s)
s.age


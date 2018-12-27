#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午11:50
# @Author  : Ryan Xu
# @Site    : 
# @File    : recursion.py
# @Software: PyCharm


class recursion(object):

    def fact(self, num):
        if isinstance(num, int):
            if num==1:
                return 1
            return num * self.fact(num-1)

    def move(self):

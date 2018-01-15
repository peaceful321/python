#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午8:38
# @Author  : Ryan Xu
# @Site    : 
# @File    : Duck.py
# @Software: PyCharm


from basic.oop.Animal import Animal

class Duck(Animal):

    def run(self):
        print("Duck is running by two legs...")


    def fly(self):
        print("Duck is flying by wing...")


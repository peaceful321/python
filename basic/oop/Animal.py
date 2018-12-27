#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午8:29
# @Author  : Ryan Xu
# @Site    : 
# @File    : Animal.py
# @Software: PyCharm


class Animal:

    def run(self):
        print("The animal is running...")

    def __init__(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type


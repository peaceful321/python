#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 6:58 PM
# @Author  : Ryan Xu
# @Site    : 
# @File    : learnClass.py
# @Software: PyCharm


class Dog:

    def __init__(self, dogName, dogColor, dogKind, dogAge):
        self.name = dogName
        self.color = dogColor
        self.kind = dogKind
        self.age = dogAge

    def selfDesc(self):
        print("大家好！我叫 " + self.name + " 是一只 "
              + self.kind + " ，今年" + str(self.age) + "岁了，" + "你们也看到了，我是" + self.color + "色的")




if __name__ == '__main__':

    dog1 = Dog('lele', "白", "二哈", 2)
    dog1.selfDesc()

    dog2 = Dog('小科', '黑', '中华田园犬', 3)
    dog2.selfDesc()

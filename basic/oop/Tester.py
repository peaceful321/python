#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午8:38
# @Author  : Ryan Xu
# @Site    : 
# @File    : Tester.py
# @Software: PyCharm

from basic.oop.Animal import Animal
from basic.oop.Duck import Duck
from basic.oop.Dog import Dog


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):

    def run(self):
        print("Tortoise is running slowly...")


class Clock():
    def run(self):
        print("The clock is running...")



if (__name__ == "__main__"):
    dog = Dog()
    duck = Duck()

    dog.run()
    duck.run()

    ml = list()

    print(
        isinstance(dog, Dog),
        isinstance(dog, Animal),
        isinstance(duck, Duck),
        isinstance(duck, Animal),
        isinstance(ml, Animal)
    )


    #开闭原则：允许新增Animal 的子类 (Tortoise)， 但不需要修改依赖 Animal 类型的 run_twice()方法的实现
    #对扩展开放，对修改封闭  （多态）
    run_twice(dog)
    run_twice(Duck())
    run_twice(Tortoise())

    #动态语言的"鸭子类型"， 对继承没有严格要求， 一个对象只要"看起来像鸭子， 走起来想鸭子"， 那它就是鸭子。eg: Python的"file-like object"就是一种鸭子类型
    #和Java 这样的静态语言不一样， 必须是继承 Animal类型才能传入 run_twice 方法中
    run_twice(Clock())




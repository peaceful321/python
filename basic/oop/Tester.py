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
    #对扩展开放，对修改封闭
    run_twice(dog)
    run_twice(Duck())

    run_twice(Tortoise())





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午4:03
# @Author  : Ryan Xu
# @Site    : 
# @File    : EnumDemo.py
# @Software: PyCharm

from enum import Enum, unique


month = Enum('Month', ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

for name, member in month.__members__.items():
    print(name, '=>', member, ',', member.value)



# @unique 装饰器 可以帮助我们坚持包子没有重复值

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sun)

d = Weekday.Tue
print(d)
print(d.value)

print(d == Weekday.Tue)
print(d == Weekday.Sun)
print(d == Weekday(2))
print(Weekday(5))

for name, member in Weekday.__members__.items():
    print(name, "=>", member)



## 小结： Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。








#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 下午1:19
# @Author  : Ryan Xu
# @Site    : 
# @File    : user_enum.py
# @Software: PyCharm


from enum import Enum, unique


#使用枚举
month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in month.__members__.items():
    print(name, '=>', member, ',', member.value)




@unique
class Weekday(Enum):
    Sunday = 0,
    Monday = 1,
    Tuesday = 2,
    Wednesday = 3,
    Thursday = 4,
    Friday = 5,
    Saturday = 6


#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Month(Enum):
    January = 1,
    February = 2,
    March = 3,
    April = 4,
    May = 5,
    June = 6,
    July = 7,
    August = 8,
    September = 9,
    October = 10,
    November = 11,
    December = 12








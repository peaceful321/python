#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午10:16
# @Author  : Ryan Xu
# @File    : use_slots.py


class Students(object):
    __slots__ = ("stuId", "stuName") #用Tuple 定义允许绑定的属性名称


#__slots_可以限制类属性， 但仅对当前类有效， 对子类无效
class GraduateStudents(Students):
    pass


s1 = Students()

s1.stuId = "100001"
s1.stuName = "Anne"

try:
    print(s1.stuId, s1.stuName)
    s1.stuAge = "18"   #AttributeError: 'Students' object has no attribute 'stuAge'
except AttributeError as e:
    print("AttributeError:", e)

gs = GraduateStudents()

gs.stuAge = 18

print(gs.stuAge)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 上午10:39
# @Author  : Ryan Xu
# @Site    : 
# @File    : use_property.py
# @Software: PyCharm

class Student(object):

    @property
    def score(self):
        '''@property ，类似java 中的 getter 方法, 但该方法名， 直接当属性使用'''
        return self._score

    @score.setter
    def score(self, value):
        '''
        类似java 中的 setter 方法
        
        :param value: 
        :return: 
        '''
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must betweeb 0 and 100")
        self._score = value


    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, day):
        self._birthday = day


    @property
    def age(self):
        '''
        age 是一个只读属性， 不可以setter 
        可以通过当前年份 - birthday 中的年 粗略计算获取
        :return: 
        '''
        return 2018 - int(self.birthday[0:4])



s = Student()
s.birthday = "1992-08-20"
print(s.age)

s.score = 98
print('s.score = ', s.score)
print('s.score = ', s.score)


# s1 = Student()
# s1.score = 101
# print('s.score = ', s1.score)
# print('s.score = ', s1.score)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 7:00 PM
# @Author  : Ryan Xu
# @Site    :
# @File    : learnFunction.py
# @Software: PyCharm


# 语法 def 函数名():

# def add():
#     return 5 + 3
#
# result = add()
# print(result)


# def add2(a, b):
#     return a + b
#
# r = add2(3, 5)
# print(r)
#
# def sum(num):
#     sum = 0
#     for i in range(num):
#         sum = sum + i
#     return sum
#
# s = sum(11)
# print(s)


# 该函数用于求平均值， 可以接受任意长度的变量
# def avg(first, *rest):
#     return (first + sum(rest)) / (1 + len(rest))
#
#
# result = avg(2, 10, 10, 10, 10)
# print(result)


#
#
#
# def adminAvg(first, *rest):
#     sum = first
#     count = 1
#     for r in rest:
#         sum = sum + r
#         count += 1 #count = count + 1
#
#     result = sum / count
#     return result
#
#
# print(adminAvg(1, 3, 5, 7, 9, 10))
#
#

mList = [['lili', 50, 'female'], ['dandan', 48, 'male'], ['guoting', 52, 'male']]

#['lili', 50, 'female']
#['dandan', 48, 'male']
#['guoting', 52, 'male']
#

c = 0
for l in mList:
    for p in l:
        if c == 5:
            break
        print(p)
        c += 1



#
# for l in mList:
#     gender = '男'
#     if l[2] == 'female':
#         gender = '女'
#     else:
#         gender = '男'
#
#     print('大家好，我叫' + l[0] + '， 我有 ' + str(l[1]) +'kg，我是 ' + gender + '生。')









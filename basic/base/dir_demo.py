#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 下午8:01
# @Author  : Ryan Xu
# @Site    : 
# @File    : dir_demo.py
# @Software: PyCharm


from datetime import datetime
import os

pwd = os.path.abspath('.')

print(' Size    Last Modified       Name')

print('----------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = "/" if os.path.isdir(f) else ''
    print('%10d    %s    %s%s' %(fsize, mtime, f, flag))
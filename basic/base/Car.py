#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 7:26 PM
# @Author  : Ryan Xu
# @Site    : 
# @File    : Car.py
# @Software: PyCharm


class Car:

    def __init__(self, type, carName, size):
        self.type = type
        self.name = carName
        self.size = size

    def drive(self, driveType, isElectricity, overSpeed):
        '''
        
        :param driveType: 自动档:c2 or 手动挡:c1
        :param isElectricity: 是否有电 0：无， 1：有
        :param overSpeed: 速度 0:没超速， 1：超速
        :return: 
        '''
        if driveType == 'c1':
            print("安全带，踩离合，点刹车，放手刹，挂一档，开起步灯")
        else:
            print("安全带，踩刹车，挂D档，开起步灯")

        if isElectricity == 0:
            print("找充电桩进行充电，休息")
        else:
            print("继续开......")
        if overSpeed == 1:
            print("点刹车，减速到60码")
        else:
            print("踩油门，冲啊，马上到家了")

if __name__ == "__main__":

    bwm = Car("bwm x6", "bwm", 5)
    bc = Car('benci one', 'bc', 8)
    print("这辆车叫" + bwm.name + ",款式是" + bwm.type + ", 能载" + str(bwm.size) + "人")
    print("这辆车叫" + bc.name + ",款式是" + bc.type + ", 能载" + str(bc.size) + "人")

    # 开车
    bwm.drive('c1', 1, 0)
    bc.drive('c2', 0, 1)


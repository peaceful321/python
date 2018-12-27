#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 9:07 AM
# @Author  : Ryan Xu
# @Site    : 
# @File    : ImageRound.py
# @Software: PyCharm

from qiniu import Auth, PersistentFop, urlsafe_base64_encode

#定义/创建 一个类 ImageRound
class ImageRound:

    #指定成员变量
    AK = "xbUKI2_zoxvHiFr2p5A0qR1xprDnleaBd6CJdJ60"
    SK = "k4u0vG7JxMfG-IRZgvdV8ERH95Ucl66KSnRxqHi9"

    # 定义一个方法，负责处理已有图片，将其变为圆形
    def roundPic(self, bn, key):
        """
        触发持久化
        :param bn: 空间名称
        :param key: 文件名称
        :return: 
        """
        #创建授权对象
        auth = Auth(self.AK, self.SK)
        #指定 私有队列
        pipeline = "image-pipeline"
        #指定数据处理操作
        fops = "roundPic/radius/!50p"
        #定义另存的文件名称
        new_key = "round_" + key
        #另存的编码
        saveAs = urlsafe_base64_encode(bn + ":" + new_key)
        #管道拼接
        fops = fops + "|saveas/" + saveAs
        #创建数据处理对象 pfop
        pfop = PersistentFop(auth=auth, bucket=bn, pipeline=pipeline)
        ops = []
        ops.append(fops)
        #执行数据处理 execute
        r, i = pfop.execute(key, ops, 1)
        #查看处理信息
        print(i)

#创建对象， 并通过该对象调用 roundPic方法
if __name__ == "__main__":
    imageRound = ImageRound()
    imageRound.roundPic("test-bucket", "20180115z/a0.jpg")
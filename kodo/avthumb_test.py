#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 下午8:29
# @Author  : Ryan Xu
# @Site    : 
# @File    : avthumb_test.py
# @Software: PyCharm
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
from common.AccountMgr import AccountMgr

def save_mp3():
    access_key = '0ZT-Rd0AswhPQti5lX2Ytt1T6XkyM80eY_4w9Pm9'
    secret_key = 'MbscrgLx_FefkUZ21SjY-GRE1oPJcvP2vvN6oXgW'

    # 初始化Auth状态
    q = Auth(access_key, secret_key)

    # 你要测试的空间， 并且这个key在你空间中存在
    bucket_name = 'live-bucket'
    key = 'mayun12_13.mp4'

    # 指定转码使用的队列名称
    pipeline = 'image-pipeline'

    # 设置转码参数（以视频转码为例）
    fops = 'avthumb/mp3/ar/48000/vn/1|saveas/'

    # 通过添加'|saveas'参数，指定处理后的文件保存的bucket和key，不指定默认保存在当前空间，bucket_saved为目标bucket，bucket_saved为目标key
    saveas_key = urlsafe_base64_encode(bucket_name + ':mayun_mp3_test.mp3')

    fops = fops + saveas_key

    # 在上传策略中指定fobs和pipeline
    policy = {
      'persistentOps': fops,
      'persistentPipeline': pipeline
     }

    token = q.upload_token(bucket_name, key, 3600, policy)

    localfile = '/Users/ryanxu/Downloads/mayun.mp4'

    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)


if(__name__ == "__main__"):
    save_mp3()



from qiniu import Auth, PersistentFop, build_op, op_save, urlsafe_base64_encode
from common.AccountMgr import AccountMgr

accountMgr = AccountMgr()
accessKey = accountMgr.getAccessKey()
secretKey = accountMgr.getSecretKey()


def waterMark():
    '''
    已上传的图片打水印
    :return: 
    '''

    #1、指定 空间绑定的域名、 水印图片地址、 空间名称、 空间水印原图Key、 私有处理队列
    domain = "test.zhaojianfeng.cn"
    wmImg = "https://olhvkds73.qnssl.com/logo.png"
    bucket = "test-bucket"
    key = "a0.jpg"
    pipeline = "image-pipeline"
    encodeWmImg = urlsafe_base64_encode(wmImg)

    #2、创建Auth对象、 指定fops 操作、 saveas接口及签名
    auth = Auth(access_key=accessKey, secret_key=secretKey)
    fops = "watermark/1/image/" + encodeWmImg + "/gravity/SouthWest"
    saveKey = urlsafe_base64_encode(bucket + ":" + "p111_a0.jpg")
    fops = fops + "|saveas/" + saveKey
    signTarget = domain + "/" + key + "?" + fops
    sign = urlsafe_base64_encode(signTarget)
    fops = fops + "/sign/" + sign

    #3、执行持久化操作
    pfop = PersistentFop(auth=auth, bucket=bucket, pipeline=pipeline)
    ops = []
    ops.append(fops)
    ret, info = pfop.execute(key, ops)

    #4、查看执行结果
    print(info)
    assert ret['persistentId'] is not None



if(__name__ == "__main__"):
    waterMark()

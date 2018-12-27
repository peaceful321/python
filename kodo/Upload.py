from qiniu import Auth, put_file, etag
from common.AccountMgr import AccountMgr
# ACCESS_KEY = "0ZT-Rd0AswhPQti5lX2Ytt1T6XkyM80eY_4w9Pm9"
# SECRET_KEY = "MbscrgLx_FefkUZ21SjY-GRE1oPJcvP2vvN6oXgW"


accountMgr = AccountMgr()
ACCESS_KEY = accountMgr.getAccessKey()
SECRET_KEY = accountMgr.getSecretKey()

def upload():
    '''
    简单上传
    :return: 
    '''

    auth = Auth(ACCESS_KEY, SECRET_KEY)
    bucket = "test-bucket"
    key = "97p58PICV26_222.jpg"

    uploadToken = auth.upload_token(bucket, key, 3600)
    filePath = "/Users/ryanxu/Downloads/imgs/stage.jpg"

    ret, info = put_file(up_token=uploadToken, key=key, file_path=filePath)
    print(info)


def overrideUpload(targetKey):
    '''
    覆盖上传
    :param targetKey: 
    :return: 
    '''
    auth = Auth(ACCESS_KEY, SECRET_KEY)
    bucketName = "test-bucket"
    token = auth.upload_token(bucket=bucketName, key=targetKey, expires=3600)
    filePath = "/Users/ryanxu/Downloads/bg.jpg"


    ret, info = put_file(token, targetKey, filePath)
    print(ret)
    print(info)


if(__name__ == "__main__"):
    # overrideUpload('bg.jpg')
    upload()


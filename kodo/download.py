from qiniu import Auth, urlsafe_base64_encode
from common.AccountMgr import AccountMgr
import requests, json, array, re, os

'''
author: xuhuanchao
date: 2017-07-11
AccountMgr 是自己定义的模块，存放了AK, SK 等账号信息
'''
accountMgr = AccountMgr()
accessKey = accountMgr.getAccessKey()
secretKey = accountMgr.getSecretKey()

#通过AK, SK 创建 auth对象
auth = Auth(accessKey, secretKey)


def __getDownloadUrl(bucketName, key):
    '''
    获取下载的URL
    :param bucketName: 空间名称
    :param key: 空间存储的文件名称
    :return: 
    '''
    flag = __isPrivateBucket(bucketName)
    domainList = getDomainByBucket(bucketName)
    print(domainList)
    domain = ''
    for i in range(len(domainList)):
        pattern = re.compile("[a-z0-9.]*clouddn.com]")
        match = pattern.match(domainList[i])
        if match:
            continue
        else:
            domain = domainList[i]

    #如果空间没有绑定自定义域名， 则使用测试域名
    if(domain == ''):
        domain = domainList[0]

    baseUrl = "http://" + domain + "/" + key
    if(flag):
        downloadUrl = auth.private_download_url(baseUrl)
    else:
        downloadUrl = baseUrl
    return downloadUrl


def __isPrivateBucket(bucketName):
    '''
    判断是否是私有空间， 用admin 开头命名的空间都是 私有空间;  tips: 自己的业务控制
    :param bucketName: 空间名称
    :return: bool
    '''
    if bucketName == "admin" or bucketName[0:5] == "admin":
        return True
    else:
        return False


def getDomainByBucket(bucketName):
    '''
    通过七牛云接口， 获取空间绑定的域名
    参考文档：https://developer.qiniu.com/kodo/api/1612/bucket-domainlist
    :param bucketName:  空间名称
    :return: list of bucket's domain
    '''
    connector = "/v6/domain/list?tbl={0}".format(bucketName)
    url = "http://api.qiniu.com" + connector
    try:
        accessToken = auth.token_of_request(connector)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "QBox " + accessToken
        }
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        if(resp.status_code == requests.codes.ok):
            return list(resp.json())

    except Exception as e:
        print("出现异常...信息如下：\n" + e)

def download(bucketName, key, localPath):
    '''
    开始下载
    :param bucketName: 空间名称
    :param key: 下载的文件名称
    :param localPath: 存储到本地的路径
    :return: None
    '''
    downloadUrl = __getDownloadUrl(bucketName, key)
    print(downloadUrl)
    resp = requests.get(downloadUrl)
    path = localPath + "/" + key
    with open(path, 'wb+') as f:
        f.write(resp.content)


#程序的主入口，类似java 的main 函数
if(__name__ == "__main__"):
    bucketName = "test-bucket"
    key = "stage111.jpg"
    localPath = "/Users/ryanxu/Documents"
    download(bucketName, key, localPath)

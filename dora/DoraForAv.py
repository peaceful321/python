from qiniu import Auth, urlsafe_base64_encode, PersistentFop
from common.AccountMgr import AccountMgr

class AvConcat:

    def ops(self, urlList):
        ak = AccountMgr().getAccessKey()
        sk = AccountMgr().getSecretKey()
        auth = Auth(ak, sk)
        domain = "test.zhaojianfeng.cn"
        pipeline = "av-pipeline"
        bucket = "test-bucket"
        key = "mayun0.mp4"
        mSaveAs = urlsafe_base64_encode(bucket + ":mayun_all.mp4")

        encodeUrls = []
        for i in range(len(urlList)):
            encodeUrls.append(urlsafe_base64_encode(urlList[i]))
        fops = "avconcat/2/format/mp4/" + "/".join(encodeUrls) + "|saveas/" + mSaveAs
        print(fops)
        sign = urlsafe_base64_encode(domain + "/" + key + "?" + fops)
        fops = fops + "/sign/" + sign

        pfops = PersistentFop(auth, bucket, pipeline)
        ops = []
        ops.append(fops)
        ret, info = pfops.execute(key, ops)
        print(info)
        assert ret['persistentId'] is not None


if(__name__ == "__main__"):
    avConcat = AvConcat()
    domain = "test.zhaojianfeng.cn"
    urlList = []
    urlList.append("http://" + domain + "/mayun1.mp4")
    urlList.append("http://" + domain + "/mayun2.mp4")
    avConcat.ops(urlList)



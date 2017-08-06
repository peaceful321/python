from qiniu import Auth, PersistentFop, build_op, op_save, urlsafe_base64_encode
from common.AccountMgr import AccountMgr

# 对已经上传到七牛的视频发起异步转码操作
access_key = AccountMgr().getAccessKey()
secret_key = AccountMgr().getSecretKey()
q = Auth(access_key, secret_key)

# 要转码的文件所在的空间和文件名。
bucket_name = 'test-bucket'
key = 'mayun0.mp4'

# 是使用的队列名称,不设置代表不使用私有队列，使用公有队列。
pipeline = 'av-pipeline'

# 要进行转码的转码操作。
fops = 'avthumb/mp4/vb/128k'

# 可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
saveas_key = urlsafe_base64_encode('test-bucket:compress222.mp4')

fops = fops+'|saveas/'+saveas_key
mSign = "test.zhaojianfeng.cn" + "/" + key + "?" + fops
fops = fops + "/sign/" + mSign

pfop = PersistentFop(q, bucket_name, pipeline)
ops = []
ops.append(fops)
ret, info = pfop.execute(key, ops, 1)
print(info)
assert ret['persistentId'] is not None
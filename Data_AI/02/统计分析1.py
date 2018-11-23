import numpy as np
#
#
# arr1 = np.array([[1,2],[3,4]])
# # 以二进制保存,默认扩展名：npy
# np.save('data',arr1)
#
# # 读取；要加扩展名
# data = np.load('data.npy')
# print(data)
#
#
#
# np.savetxt('data.txt',arr1,fmt='%d',delimiter=',')
# # delimiter='' ;分隔符
# data2 = np.loadtxt('data.txt',dtype=np.int32,delimiter=',')
# print(data2)


n_type = np.dtype([('name',np.str_,40),('num',np.int64),('location',np.str_,20)])
data3 = np.loadtxt('job.txt',dtype=n_type,delimiter=',',encoding='utf-8')
print(data3)
# da = np.array(data3,dtype=n_type)
# print(da)










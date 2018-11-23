#-*- coding:utf-8 -*-

import numpy as np

#一维
arr1 = np.array([1,2,3])

#秩
print('秩：',arr1.ndim)  #1
#轴
print('轴：',arr1.shape)  #(3,),


#二维
arr2 = np.array([[1,2,3,0],
		[4,5,6,0],
		[7,8,9,0]])

#秩
print('秩：',arr2.ndim)  #2
#轴
print('轴：',arr2.shape)  #(3,4)

#第一个[]行，第里面的[]列

print(arr2.size) #12
print(arr2.dtype) #int32
print('每个元素大小：',arr2.itemsize) #4个字节
print('缓冲区：',arr2.data) #











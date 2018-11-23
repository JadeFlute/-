import numpy as np

# 数组变换形态
arr1 = np.array([1,2,3,4,5,6])  #一维
print(arr1.shape)

arr2 = arr1.reshape(2,3)
print(arr2,arr2.shape)

arr3 = arr1.reshape(6,1)    #二维
print(arr3,arr3.ndim,arr3.shape)


a = np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]])
print(a.shape)
# 参数为-1时，会自动计算列
a_1 =a.reshape(2,-1)
print(a_1)
#列为空，为一维数组
a_2 = a.reshape(-1,)
print(a_2)
#同上
a_3 = a.reshape(-1)
print(a_3)
# 16行，1列
a_4 = a.reshape(-1,1)
print(a_4)

#数组过大的时候，numpy自动省略中间部分，显示两天
arr5 = np.arange(10000).reshape(100,100)
print(arr5)
#修改设置，输出全部
np.set_printoptions(threshold=np.NAN)
arr5 = np.arange(10000).reshape(100,100)
print(arr5)












import numpy as np

arr = np.arange(5)
# 生成两遍arr
arr1 = np.tile(arr,2)
print(arr1)
# [0 1 2 3 4 0 1 2 3 4]


arr2 = arr1.reshape(2,5)
print(arr2)


# 列方向，额外重复2遍
arr3 = np.repeat([[1],[2],[3]],3,axis=1)
print(arr3)
# [[1 1 1]
#  [2 2 2]
#  [3 3 3]]












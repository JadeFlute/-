import numpy as np

arr1 = np.array([[1,1,3,3],
                [2,2,5,5]])

# 横向切割成2份
arr2 = np.hsplit(arr1,2)
print(arr2)
# [array([[1, 1],
#        [2, 2]]),
#  array([[3, 3],
#        [5, 5]])]

arr3 = np.split(arr1,2,axis=1)
print(arr3)

#纵向切割完，还是二维数组
arr4 = np.vsplit(arr1,2)
print(arr4)
# [array([[1, 1, 3, 3]]), array([[2, 2, 5, 5]])]


arr5 = np.split(arr1,2,axis=0)
print(arr5)



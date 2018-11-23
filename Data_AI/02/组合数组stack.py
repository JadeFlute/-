import numpy as np

# hstack()/vstack()
arr1 = np.arange(1,6,2)
arr2 = np.arange(7,12,2)

#横向拼接
arr3 = np.hstack((arr1,arr2))
print(arr3)
# [ 1  3  5  7  9 11]

#纵向拼接
arr4 = np.vstack((arr1,arr2))
print(arr4)
# [[ 1  3  5]
#  [ 7  9 11]]


#concatenate()
#横向：axis=1
#纵向：axis=0
arr1 = np.array([[1,1],[2,2]])
arr2 = np.array([[1,1],[2,2]])
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)
# [[1 1 1 1]
#  [2 2 2 2]]


# stack:可以用中括号


































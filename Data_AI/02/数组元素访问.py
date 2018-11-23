import numpy as np

# arr = np.arange(10)
# print(arr)
# print(arr[5])
# print(arr[3:5]) #左闭右开
# arr[3:5] = 100,200
# print(arr[-1])
# print(arr[1:-1:2])


ar = np.array([[1,2,3,4],
               [5,6,7,8],
               [7,8,9,0]])
#ar[行标，列标]
print(ar[0,1:3])
# [2 3]

print(ar[1:,2:])
# [[7 8]
#  [9 0]]

#取出 第0行，第1个数；第1行，第2个数，第2行，第3个数
new_ar = ar[(0,1,2),(1,2,3)]

#第1行后的所有行，第0,2,3列的值
ar1 = ar[1:,(0,2,3)]

# 真假真
mask = np.array([1,0,1],dtype=np.bool)

#取出，第二列中为真的值
print(ar[mask,2])


























import numpy as np

arr = np.array([[4,3,2],
                [2,1,5]])
print(arr)
#默认按照行排序
# arr.sort()
# print(arr)
# [[2 3 4]
#  [1 2 5]]

# 按列排序
# arr.sort(axis=0)
# print(arr)
# # [[2 1 2]
# #  [4 3 5]]

# 间接排序：将排序后的下标输出，不更改物理结构
res = arr.argsort()
print(res)
# [[2 1 0]
#  [1 0 2]]

# 传多个，只排序最后一个；间接排序
np.lexsort(arr)



# lst = [2,4,3]
# # 修改lst本身
# lst.sort()
# print(lst)
#
# # 排序后，返回一个新列表
# lst2 = sorted(lst)



























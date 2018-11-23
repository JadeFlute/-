import numpy as np

arr = np.arange(20).reshape(4,5)
# 元素总和
print(np.sum(arr))
# 每一步，进行求和
print(np.cumsum(arr))
# [  0   1   3   6  10  15  21  28  36  45  55  66  78  91 105 120 136 153
#  171 190]
# 平均数
print(np.mean(arr),np.sum(arr)/arr.shape[0]*arr.shape[1])





























































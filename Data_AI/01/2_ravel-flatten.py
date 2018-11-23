import numpy as np

# ravel：数组的展平操作;reshape的逆操作
a1 = np.arange(10)
a2 = a1.reshape(2,5)
print(a1,a2)

a3 = a2.ravel()
print(a3)

# flatten:默认横向展平；
# 纵向展平需要加 'F' :每一列拿出来，放一行
a4 = a2.flatten()
print(a4)

a5 = a2.flatten('F')
print(a5)

#ravel,flatten:区别
# 共同点：将多维数组降为一维数组
# 区别：flatten:返回的是拷贝,ravel:视图

#flatten:对拷贝进行修改，不会影响原数组；
#ravel:会影响






















import numpy as np
import matplotlib.pyplot as mp


# 0-1之间的随机数,3个
r1 = np.random.random(3)

# 两行三列，矩阵
r2 = np.random.rand(2,3)

#1000个符合正态分布的随机数
r3 = np.random.randn(1000)

# mp.hist(r3)
# mp.show()

# 生成一个3-5之间的整数;左包右包
r4 = np.random.randint(1,5)
print(r4)

r5 = np.random.randint(2,10,size=(2,5))
print(r5)
# [[9 3 3 5 7]
#  [4 6 3 2 5]]


# 卡方检验





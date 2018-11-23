import numpy as np

# array()
# object:接收的array；表示想要创建的数组
# dtype：接收data-type,表示数组所需的数据类型，如果未给定，则选择保存对象所需的最小类型
# ndmin：接收int；最小维度
a1 = np.array([1,2,3,4])

a2 = np.array([1,2,3.14,5]) #浮点型

a3 = np.array([1,2,3.14,5],dtype='int32')

a4 = np.array([(1,2),(3,4)])

#(初始值，终止值，步长)，左包右不包
a6 = np.arange(0,1,0.1)
# [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
print(a6)


a7 = np.arange(0,1,0.22)
print(a7)
# 缺点：元素个数预估有难度

#linspace(初始值，终止值，元素个数)
# 左包右包
a8 = np.linspace(0.1,1,10)
print(a8)
# [0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]


#logspace()
#生成10^1到10^3之间的等比例数;比例为10
a9 = np.logspace(1,3,3)
print(a9)
# [  10.  100. 1000.]

# 占位函数
a11 = np.zeros((2,3))
#两行三列，用0填充

a12 = np.ones((2,3))

# empty()函数,2行3列随机数
a13 = np.empty((2,3))
print(a13)

# eye(N)
#生成N阶矩阵，并且对角线元素为1
a14 = np.eye(3)
print('eye:\n',a14)
 # [[1. 0. 0.]
 # [0. 1. 0.]
 # [0. 0. 1.]]


a15 = np.diag([1,2,3,4])
print(a15)
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]













import numpy as np

#创建矩阵
A = np.mat('1 0 0 0;0 2 0 0;0 0 3 0;0 0 0 4')
print(A)
B = np.mat([[1,1],[2,2],[3,3],[4,4]])
print(B)
# matrix函数创建矩阵
C = np.matrix('1 0 0 0;0 2 0 0;0 0 3 0;0 0 0 4')
print(C)

D = np.matrix([[1,1],[2,2],[3,3],[4,4]])
print(D)


# bmat
#通过分块矩阵创建大矩阵
E1 = np.bmat('A B;C D')
# E2 = np.matrix([[A,B],[C,D]])
print(E1)
# print(E2)


#矩阵运算
A = np.matrix([[1,2],[3,4]])
B = 2*A
print(B)

arr1 = np.ones((2,2))
A = 5*np.matrix(arr1)
print(A)

#矩阵相乘

A = np.mat('1 0 0 0;0 2 0 0;0 0 3 0;0 0 0 4')
B = np.mat('1 0 0 1;0 2 0 2;0 0 3 3;4 0 0 4')
C = A*B
print(C)

#转置:行变列
print(C.T)















































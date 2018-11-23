import numpy as np

# 读取数据
data = np.loadtxt('iris_sepal_length.csv')
print(data)
# 排序
data.sort()
print(data)
# 去重
data2 = np.unique(data)
print(data2)

# 统计
print('元素总和:',np.sum(data2))
print('均值:',np.mean(data2))
# 标准差和方差，要使用原数据，不能用去重后的。
print('标准差：',np.std(data))
print('方差：',np.var(data))

print('最大值：',np.max(data2))
print('最小值：',np.min(data2))




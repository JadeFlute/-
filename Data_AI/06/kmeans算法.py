import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 读取数据；

data = pd.read_csv('company.csv',encoding='gbk')

# 将数据转成二维数组（矩阵）；
# 取出后两列数据；
# [['平均每次消费金额','平均消费周期（天）']].as_matrix()
# .as_matrix()[:,1:]

print(data)

# 聚类---K-means
from sklearn.cluster import KMeans
# 将数据分成三组；
kms = KMeans(n_clusters=3)
result = kms.fit_predict(data)
print(result)

# 可视化
plt.figure()

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('消费周期（天）')
plt.ylabel('消费金额')

for i in range(0,len(result)):
    if result[i] == 0:
        y = data.iloc[i, 1]
        x = data.iloc[i, 2]
        plt.plot(x, y, '*r')
    elif result[i] == 1:
        y = data.iloc[i, 1]
        x = data.iloc[i, 2]
        plt.plot(x, y, '*b')
    elif result[i] == 2:
        y = data.iloc[i, 1]
        x = data.iloc[i, 2]
        plt.plot(x, y, '*g')



plt.show()






























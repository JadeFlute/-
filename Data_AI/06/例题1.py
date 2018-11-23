import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 要根据时间来获取数据

data = pd.read_csv('NBA.csv',encoding='gbk')
print(data)

new_data = data[['得分效率','助攻效率']].as_matrix()
kms = KMeans(n_clusters=3)
result = kms.fit_predict(new_data)
print(result)


plt.figure()

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('得分效率')
plt.ylabel('助攻效率')

for i in range(len(result)):
    if result[i] == 0:
        x = data.iloc[i,4]
        y = data.iloc[i,2]
        plt.plot(x,y,'*r')
    elif result[i] == 1:
        x = data.iloc[i,4]
        y = data.iloc[i,2]
        plt.plot(x,y,'*g')
    elif result[i] == 2:
        x = data.iloc[i,4]
        y = data.iloc[i,2]
        plt.plot(x,y,'*b')

plt.show()







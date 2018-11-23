import matplotlib.pyplot as plt
import numpy as np

# 为了正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 为了正常显示 '-'
plt.rcParams['axes.unicode_minus'] = False

data = np.load('国民经济核算季度数据.npz')
# 获取列名
name = data['columns']
# 获取列值
values = data['values']
# 获取所有数；不省略
np.set_printoptions(threshold=np.NaN)
# print(name,values)

plt.figure(figsize=(8,5))

x = range(3)
#最后一行，下标，3-5列
y = values[-1,3:6]

plt.title('2017第一季度国民生产总值直方图')
plt.xlabel('产业')
plt.ylabel('生产总值')
plt.xticks(range(3),['第一产业','第二产业','第三产业'])
# 直方图
plt.bar(x,y,width=0.2)

plt.show()



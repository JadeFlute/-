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
print(name,values)

plt.figure(figsize=(8,5))

x = range(3)
#最后一行，下标，3-5列
y = values[-1,3:6]

# 各区域分隔；作用：强调
exp = [0.1,0.01,0.01]
labels = ['第一产业','第二产业','第三产业']

#饼状图;autopct:小数点保留一位
plt.pie(y,explode=exp,labels=labels,autopct='%1.1f%%')

plt.title('2017第一季度国民生产总值饼状图')
# plt.xlabel('产业')
# plt.ylabel('生产总值')
# plt.xticks(range(3),['第一产业','第二产业','第三产业'])


plt.show()

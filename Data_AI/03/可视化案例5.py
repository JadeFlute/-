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
# np.set_printoptions(threshold=np.NaN)

# 所有行，第一列
x = values[:,1]
# 所有行，第二列
y = values[:,2]

plt.figure(figsize=(8,5))

# # 散点图；圆形；c:颜色，黑色是：k
# plt.scatter(x,y,marker='o')
#
# # 四个季度，步长设置为4；
# plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
# plt.title('2000-2017国民生产总值散点图')

# 折线图
plt.plot(x,y,color='r',linestyle='--',marker='o')
plt.title('2000-2017国民生产总值折线图')
plt.xlabel('年份')
plt.ylabel('生产总值(亿)')
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)


plt.savefig('国民生产总值折线图.png')

plt.show()

















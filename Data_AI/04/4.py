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

x = range(9)
#最后一行，下标，3-5列
y = values[1,6:]

plt.title('2000年第一季度各产业国民生产总值饼状图')
# 9个
# 各区域分隔；作用：强调
# exp = [0.1,0.01,0.01]
labels = ['农林牧渔业', '工业', '建筑业',
 '批发和零售业', '交通运输、仓储和邮政业', '住宿和餐饮业',
 '金融业' ,'房地产业', '其他行业']

#饼状图;autopct:小数点保留一位
plt.pie(y,labels=labels,autopct='%1.1f%%')

plt.title('2000第一季度国民生产总值饼状图')

plt.show()
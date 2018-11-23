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

plt.figure(figsize=(8,7))

x = range(9)
#最后一行，下标，3-5列
y = values[1,6:]

plt.title('2000年第一季度各产业国民生产总值直方图')
plt.xlabel('产业')
plt.ylabel('生产总值(亿元)')
# 9个
xvalue = ['农林牧渔业', '工业', '建筑业',
 '批发和零售业', '交通运输、仓储和邮政业', '住宿和餐饮业',
 '金融业' ,'房地产业', '其他行业']
plt.xticks(range(0,9),xvalue[0:9],rotation=45)

# 直方图
plt.bar(x,y)

plt.show()


import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1,1,50)
y1 = 2*x+1
y2 = 2*x+2

plt.figure()

# 把数值型刻度，替换成对应的文字刻度
plt.xticks([-1,0,1],[r'$bad$',r'$normal$',r'$good$'])
# 使用plt.gca获取当前坐标轴信息
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

plt.rcParams['font.sans-serif'] = 'SimHei'
#正常显示符号；比如解决‘-’，显示成方块 问题
plt.rcParams['axes.unicode_minus'] = False

# 变量后面有逗号；因为返回值是列表；
l1, = plt.plot(x,y1)
l2, = plt.plot(x,y2)

# loc:改变图例位置
# handle:控制图形上下位置；还有：left center;center left
plt.legend(handles=[l1,l2],labels=['图例1','图例2'],loc='upper right')
# plt.legend(['y=2x+1'],loc='best')

plt.savefig('案例4')
plt.show()

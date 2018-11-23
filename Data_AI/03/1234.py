import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,1.1,0.01)
y1 = x**2
y2 = x**4
f = plt.figure(figsize=(8,6),dpi=80)
f.add_subplot(2,1,1)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
xt = np.arange(0,1.1,0.1)
plt.xticks(xt)
plt.plot(x,y1)
plt.plot(x,y2)
# 先绘制完图,再设置图例
plt.legend(['y=x^2','y=x^4'])


# 第二个视图
f.add_subplot(2,1,2)
x = np.arange(0,2*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# np.tan()

plt.xlim((0,2*np.pi))
plt.ylim((-1,1))
xt = np.arange(0,2.5*np.pi,np.pi/2)
plt.xticks(xt)

plt.plot(x,y1)
# 颜色，线宽，线样式，点状图中的点为五边形（o:圆形；p:五边形；*：星形；s：正方形）
plt.plot(x,y2,color='green',linewidth=3,linestyle='--',marker='p')

plt.legend(['y1 = sin(x)','y2 = cos(x)'])

plt.savefig('案例3.png')
plt.show()



# 上面三个小图，下面一个大图
# 第一个子视图：f.add_subplot(2,3,1)
# 第二个子视图：f.add_subplot(2,1,2)













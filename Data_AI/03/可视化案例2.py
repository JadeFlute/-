import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,1.1,0.01)
y1 = x**2
y2 = x**4

plt.figure()

plt.title('line')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
xt = np.arange(0,1.1,0.1)
plt.xticks(xt)

plt.plot(x,y1)
plt.plot(x,y2)
# 先绘制完图，载设置图例
plt.legend(['y=x^2','y=x^4'])

plt.savefig('案例2.png')
plt.show()












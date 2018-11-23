import matplotlib.pyplot as plt
import numpy as np


# 创建画布;默认白色
plt.figure()

# 构造数据集
x = np.linspace(-1,1,50)
y = 2*x + 1
# print(x,y)

# 设置属性值
plt.title('y = 2x+1')
plt.xlabel('x')
plt.ylabel('y')


#绘制
plt.plot(x,y)

# 显示
plt.show()



















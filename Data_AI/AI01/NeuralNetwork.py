#-*- coding:utf8 -*-

#反向传播算法（backpropagation）
#假设有两层：输入层：i，第一层（隐藏层）：j，第二层（输出层）：k
# 第一步：随机给值（权重，偏向）
#     输入值：Qi
#     权重：Wij
#     偏向：θj
#     通过输入值、权重和偏差计算出一个值Qj，
#           ∑(Qj*Wij)
# 第二步:(activation function)
#     将值Qj带入sigmoid函数，求出该神经节点（j节点）的值j
#   sigmoid函数（函数的曲线为S型）：
#       常用的有：
#             1.双曲函数（tanh）
#             2.逻辑函数（logistics function）即：1/(1+e^-j)
#第三步：反向更新
#       （1）计算误差
#       输出层公式：Errk=Qk(1-Qk)(Tk-Qk)   ps:Qk是计算出的本节点的值，Tk是本应该输出的值
#       隐藏层公式：Errj=Qj(1-Qj)∑Errk*Wjk
#         （2）更新权重
#         Wij（新）=Wij（旧） + ⊿Wij
#         其中：⊿Wij=l*Errj*Qi  (l是学习率learning_rate??)
#       （3）更新偏向
#       θj = θj+⊿θj
#       ⊿θj = l*Errj
#第四步：重复第三步


#本程序：两层神经网络，即：加上输入层共三层
import numpy as np

def tanh(x):
    return np.tanh(x)
#tanh的导数
def tanh_deriv(x):
    return 1 - np.tanh(x)**2

def logistic(x):
    return 1/(1+np.exp(-x))
#求导：f(x)的导数为：f(x)*(1-f(x)),so
def logistic_deriv(x):
    return logistic(x)*(1-logistic(x))

class NeuralNetwork():
    def __init__(self,layers,activation='tanh'):
        '''
        :param layers: 一个列表：存储每一层的神经节点个数（包括输入层）
        :param activation: logistic函数选择：默认tanh
        '''
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_deriv
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        self.weights = []
        # 第i层到第j层的 权重结构为 i行 j列 的二维列表
        #本次生成的权重在 -0.25到0.25 之间
        #np.random.random(2,3):生成一个2行3列的二维列表，数值都在0到1之间
        #在生成随机列表时，每一行加一位来存放偏向,最后加一行存放神经节点的值
        for i in range(1,len(layers)-1):
            self.weights.append(np.random.random((layers[i-1]+1,layers[i]+1))*0.5-0.25)
            self.weights.append(np.random.random((layers[i]+1,layers[i+1]))*0.5-0.25)

    def fit(self,X,y,learning_rate=0.2,epochs=10000):
        '''
        :param X:训练 数据集
        :param y:label（标记），即：结果
        :param learning_rate: 就是公式里的l。学习率，越小学的越仔细，学的越慢
        :param epochs:循环10000次结束。
            反向更新停止条件一般有三个：
            （1）权重低于某个阈值
            （2）预测的错误率低于某个阈值
            （3）达到预设的循环次数
        '''
        X = np.atleast_2d(X)
        #参数X至少是二维(将X转化成array类型，即：矩阵)
        temp = np.ones([X.shape[0],X.shape[1]+1])
        #创建一个临时二维列表，里面全是1，
        #假如X.shape返回值为10*100（X的行和列）
        #临时列表就是10行101列，多出来的一列用来存偏向
        temp[:,0:-1] = X
        #将X赋值给temp的所有行和除了最后一列的所有列
        X = temp
        y = np.array(y)
        #将y的类型转变成np.array型（矩阵），方便后续运算
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            #随机抽取一个行数i，将i行的数据给a,同时转成二维数组

            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l],self.weights[l])))
            #循环计算出各神经节点的值,添加到a列表中。其中np.dot为矩阵相乘

            deltas = [self.activation_deriv(a[-1])*(y[i]-a[-1])]
            #计算输出层的误差值,添加到deltas中
            #?? 带入到sidmoid的微分方程中

            for l in range(len(a)-2,0,-1):
                deltas.append(self.activation_deriv(a[l])*deltas[-1].dot(self.weights[l].T))
            #反向循环计算出隐藏层的误差。
            # 其中a列表中第一个元素为行数据，最后一个元素为输出层的值，所以都不需要。
            deltas.reverse()

            # 下面根据误差值开始反向更新：
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
                #循环更新权重，
                #layer.T.dot(delta):layer先转置再和delta求点积
                #转置：行变列，为了使结构与delta一样，
                #点积：
                # 两个向量a = [a1, a2,…, an]和b = [b1, b2,…, bn]的点积定义为：
                # a·b = a1b1 + a2b2 +……+anbn。

    def predict(self,x):
        x = np.array(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        a = temp
        for i in range(0,len(self.weights)):
            a = self.activation(np.dot(a,self.weights[i]))
        return a




































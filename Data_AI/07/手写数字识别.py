from numpy import *
import numpy as np
from os import listdir
import operator


#训练
# KNN：
# 1. 整理数据


np.set_printoptions(threshold=np.NaN)

# 读取一个文件，转换成一行
def imgv(filename):
    # 创建向量--用于存储文件的内容
    vect = zeros((1,1024))

    # 读取文件;32*32;
    fr = open(filename)
    for i in range(32):
        # 读取每行，存储在vect矩阵中,存成一行；
        row = fr.readline()
        for j in range(32):
            vect[0,32*i+j] = row[j]

    return vect

# 处理训练数据；
def train():

    # 样本数据的标签列表
    hwlabels = []

    # 读取所有训练文件的文件名
    trainfilelist = listdir('digits/trainingDigits')
    # print(trainfilelist)
    m = len(trainfilelist)

    # 创建一个大矩阵，存放所有读取到的数据
    trainmat = zeros((m,1024))

    for i in range(m):
        filename = trainfilelist[i]
        sigletrainmat = imgv('digits/trainingDigits/%s'%filename)

        # 将单个文件矩阵，放进大矩阵
        trainmat[i,:] = sigletrainmat

        # 存储类标签
        numstr = filename.split('_')[0] # 例如把 0_101.txt 中的0取出来
        hwlabels.append(int(numstr))

    # print(trainmat.shape)
    # print(len(hwlabels))
    testFunc(trainmat,hwlabels)


# 数据处理步骤：
# 读取所有文件--循环，将每个文件的32*32转换成一行，存储在一个矩阵中（单独写函数）
# -- 循环，将每个小矩阵放进大矩阵中

# 测试
def testFunc(trainingMat,hwlabels):
    # 初始化错误率
    errorcount = 0

    # 读取测试集数据
    testFileList = listdir('digits/testDigits')
    for i in range(len(testFileList)):
        fileNameStr = testFileList[i]

        # 正确标记
        trueResult = fileNameStr.split('_')[0]

        # 需要识别的标记
        fullfile = 'digits/testDigits/%s'%fileNameStr
        siglevect = imgv(fullfile)

        result = classify(siglevect,trainingMat,hwlabels,3)

        print('实际值：',trueResult)
        print('预测值：',result)
        # 预测的错误率统计
        if result != trueResult:
            errorcount += 1

    # 分类器的准确率
    truerate = 1-errorcount/len(testFileList)
    print('准确率：',truerate)


# KNN实现分类器:开始识别
# inX:要预测的样本
# dataSet：用来学习的样本
# hwlabels：学习样本的标记
def classify(inX,dataSet,hwlabels,k):
    # 2. 计算欧式距离
    # 3. 排序
    # 4. 取k个样本，做类标签的统计

    # 获取样本数据
    dataSetSize = dataSet.shape[0]

    # 矩阵计算
    # 测试的小矩阵（一行），需要和大矩阵的1934行 运算；
    # 思路二：将小矩阵广播成1934行，这样就只用运算一次就行了
    # inX : 1*1024 --> 1934*1024
    newX = tile(inX,(dataSetSize,1))

    # 计算欧式距离
    newX_2 = (newX-dataSet)**2
    # 求每一行的和
    sumX = newX_2.sum(axis=1)

    distance = sumX**0.5

    # 排序;使用间接排序，对下标进行排序，不影响原数据；
    # 因为结论标记和原数据一一对应，不能打乱顺序
    sorteddis = distance.argsort()

    numdict = {}
    # 选k值
    for i in range(k):
        # 取出邻近的样本数据；
        # 从样本结果中取出下标对应的标记
        num = hwlabels[sorteddis[i]]
        # 利用字典键值 计数，看哪个标记多
        numdict[str(num)] = numdict.get(num,0)+1

    # 对字典排序
    sorteddata = sorted(numdict.items(),key=operator.itemgetter(1),reverse=True)

    return sorteddata[0][0]


if __name__ == '__main__':
    # result = imgv('digits/trainingDigits/0_0.txt')
    # print(result)

    train()
























































































